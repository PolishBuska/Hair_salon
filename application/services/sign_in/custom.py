

from core.exceptions.user import WrongCredsException, AuthServiceError
from core.interfaces.repositories.user import UserRepositoryInterface
from core.models.login import LoginCreds


class LoginService:

    def __init__(self, repo: UserRepositoryInterface,
                 validator,
                 jwt):
        self._repo = repo
        self._validator = validator
        self._jwt = jwt

    async def login(self, creds: LoginCreds):
        """getting tokens"""
        try:

            user_by_email = await self._repo.find_one_by_email(email=creds.username)

            data = await self._validator.validate(
                                                 plain_password=creds.plain_password,
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
