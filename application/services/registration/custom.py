from sqlalchemy.exc import IntegrityError

from core.exceptions.user import AlreadyExist, RegistrationError
from core.interfaces.repositories.user import UserRepositoryInterface
from core.interfaces.services.user import UserServiceInterface

from infrastructure.hasher import PwdContext
from infrastructure.loggers.container import LoggerContainer

from core.models.user import UserWithId


class UserService(UserServiceInterface):
    def __init__(self, repo: UserRepositoryInterface):
        self._repo = repo
        self._pwd = PwdContext()
        self._logger = LoggerContainer()

    async def register(self, data: UserWithId) -> dict:
        try:
            result = await self._repo.add_user(data=data.to_dict())
            return result
        except IntegrityError as ie:
            self._logger.get_logger("WARNING").msg(f"{str(ie)}")
            raise AlreadyExist(
                f"User {data.nickname} already exist. Original error {str(ie)}"
            ) from ie
        except Exception as e:
            self._logger.get_logger("WARNING").msg(f"{str(e)}")
            raise RegistrationError(
                f"Something went wrong with the Registration event. Original error {str(e)}"
            ) from e
