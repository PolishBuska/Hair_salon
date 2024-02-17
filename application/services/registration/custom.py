from sqlalchemy.exc import IntegrityError

from domain.exceptions.user import AlreadyExist, RegistrationError
from domain.interfaces.repositories.user import UserRepositoryInterface
from domain.interfaces.services.user import UserServiceInterface

from infrastructure.hasher import PwdContext
from infrastructure.loggers.container import LoggerContainer

from domain.models.user import UserWithId


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
