
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError

from application.services.master import MasterService
from application.services.user import UserService
from application.services.login import LoginService
from application.dto.user import CurrentUserDTO

from config import get_config

from infrastructure.database import Database
from infrastructure.models import Service, User
from infrastructure.repositories.master import MasterRepository
from infrastructure.repositories.user import UserRepository
from infrastructure.adapters.jwt_handler import AuthProvider
from infrastructure.auth_validator import AuthCredValidator
from infrastructure.repositories.general import GenericRepository


def get_repository(model, repo):
    def _get_generic_repository(session: AsyncSession = Depends(Database().get_session)):
        return repo(model, session)

    return _get_generic_repository


async def get_current_user(
                           token: str = Depends(get_config().oauth2_scheme),
                           repo=Depends(get_repository(model=User,
                                                       repo=GenericRepository))):
    try:
        credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                              detail=f'Could not validate credentials',
                                              headers={"WWW-Authenticate": "Bearer"})
        token_verified = await AuthProvider().verify_access_token(token, credentials_exception)
        user = await repo.get_one(pk=token_verified.user_id)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Could not validate credentials',
                            headers={"WWW-Authenticate": "Bearer"})
    return CurrentUserDTO(user_id=user.id, role_id=user.role_id)


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
    return UserService(repo)


def login_service_factory(
        repo=Depends(get_repository(
            repo=UserRepository,
            model=User
        ))
):
    return LoginService(
        repo=repo,
        jwt=AuthProvider(),
        validator=AuthCredValidator()
    )


def current_user_stub(token: str = Depends(get_config().oauth2_scheme)):
    raise NotImplementedError


def login_service_stub():
    raise NotImplementedError


def user_service_stub():
    raise NotImplementedError


def master_service_stub():
    raise NotImplementedError
