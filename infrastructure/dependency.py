
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError

from application.services.master import MasterService
from application.services.sign_on.keycloak import UserService as KuS
from application.services.sign_on.custom import UserService
from application.services.sign_in.custom import LoginService
from application.services.sign_in.keycloak import LoginService as KcLoginService
from application.dto.user import CurrentUserDTO
from application.interactor import RegistrationInteractor

from config import get_config

from infrastructure.database import Database
from infrastructure.models import Service, User
from infrastructure.repositories.master import MasterRepository
from infrastructure.repositories.user import UserRepository
from infrastructure.adapters.jwt_handler import AuthProvider
from infrastructure.auth_validator import AuthCredValidator
from infrastructure.repositories.general import GenericRepository
from infrastructure.adapters.keycloak.admin import container_factory


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


def keycloak_login_service_factory(admin_container=Depends(container_factory)):
    return KcLoginService(admin_container)


def keycloak_service_factory(admin_container=Depends(container_factory)):
    return KuS(admin_container)


def registration_interactor_factory(
        user_service=Depends(user_service_factory),
        auth_service=Depends(keycloak_service_factory)
):
    return RegistrationInteractor(
        auth_service=auth_service,
        user_service=user_service
    )


def reg_interactor_stub():
    raise NotImplementedError


def keycloak_service_stub():
    raise NotImplementedError


def current_user_stub(token: str = Depends(get_config().oauth2_scheme)):
    raise NotImplementedError


def login_service_stub():
    raise NotImplementedError


def user_service_stub():
    raise NotImplementedError


def master_service_stub():
    raise NotImplementedError
