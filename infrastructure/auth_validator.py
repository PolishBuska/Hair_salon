"""this module provides with credentials' validator
free direct usage"""
from domain.exceptions.user import WrongCredsException, ValidatorError

from infrastructure.hasher import PwdContext

from api.schemas.user import UserReturned


class AuthCredValidator:
    """Do not expose user's password,"""

    _checker = PwdContext.pwd_context

    async def validate(self, plain_password: str, db_user: UserReturned) -> dict:
        """Validate user's creds"""
        try:
            if db_user and plain_password:
                user_data = {"user_id": db_user.id, "role_id": db_user.role_id}

                if not self._checker.verify(plain_password, db_user.password):
                    raise WrongCredsException(f"Wrong credentials")
                return user_data
        except Exception as e:
            raise ValidatorError(
                f"Something went wrong during validation event. Original error {str(e)}"
                                 ) from e
