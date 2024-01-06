from sqlalchemy.exc import IntegrityError

from domain.exceptions.user import AlreadyExist, RegistrationError
from domain.interfaces.repositories.user import UserRepositoryInterface

from infrastructure.hasher import PwdContext

from api.schemas.user import UserCreated


class UserService:
    def __init__(self, repo: UserRepositoryInterface):
        self._repo = repo
        self._pwd = PwdContext()

    async def register(self, data: UserCreated) -> dict:
        try:
            data.password = self._pwd.pwd_context.hash(data.password)
            result = await self._repo.add_user(data=data)
            return result
        except IntegrityError as ie:
            raise AlreadyExist(
                f"User {data.username} already exist. Original error {str(ie)}"
            ) from ie
        except Exception as e:
            raise RegistrationError(
                f"Something went wrong with the Registration event. Original error {str(e)}"
            ) from e
