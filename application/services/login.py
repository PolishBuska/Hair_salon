from fastapi import HTTPException

from infrastructure.auth_validator import AuthCredValidator
from infrastructure.jwt_handler import AuthProvider

from domain.exceptions.user import WrongCredsException, AuthServiceError
from domain.interfaces.repositories.user import UserRepositoryInterface


class LoginService:
    _validator = AuthCredValidator()
    _jwt = AuthProvider()

    def __init__(self, email, plain_password, repo: UserRepositoryInterface):
        self._email = email
        self._plain_password = plain_password
        self._repo = repo

    async def login(self):
        """getting tokens"""
        try:

            user_by_email = await self._repo.find_one_by_email(email=self._email)

            data = await self._validator.validate(
                                                 plain_password=self._plain_password,
                                                 db_user=user_by_email
            )
            if not data:
                raise WrongCredsException("Wrong credentials")
            access_token = await self._jwt.create_access_token(data=data)

            return {
                "access_token": access_token,
                "token_type": "bearer",
            }
        except Exception as er:
            raise AuthServiceError(
                f"Something went wrong with auth event. Original error {str(er)}"
                                   ) from er
