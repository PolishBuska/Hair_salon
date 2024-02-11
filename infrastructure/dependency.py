
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from application.services.master import MasterService
from application.services.user import UserService
from application.services.login import LoginService

from infrastructure.database import Database
from infrastructure.models import Service, User
from infrastructure.repositories.master import MasterRepository
from infrastructure.repositories.user import UserRepository
from infrastructure.adapters.jwt_handler import AuthProvider
from infrastructure.auth_validator import AuthCredValidator


def get_repository(model, repo):
    def _get_generic_repository(session: AsyncSession = Depends(Database().get_session)):
        return repo(model, session)

    return _get_generic_repository


def master_service_factory(
        repo=Depends(get_repository(
            repo=MasterRepository,
            model=Service
        ))
):
    return MasterService(repo)


def user_service_factory(
        repo=Depends(get_repository(
            repo=UserRepository,
            model=User
        ))
):
    return UserService(repo=repo)


def login_service_factory(
        repo=Depends(get_repository(
            repo=UserRepository,
            model=User
        ))
):
    return LoginService(
        repo=repo,
        jwt=AuthProvider,
        validator=AuthCredValidator
    )


def login_service_stub():
    raise NotImplementedError


def user_service_stub():
    raise NotImplementedError


def master_service_stub():
    raise NotImplementedError
