from core.exceptions.user import RegistrationError
from core.interfaces.services.user import UserServiceInterface
from core.interfaces.interactor import InteractorInterface
from core.models.user import User, UserWithId
from core.exceptions.user import AlreadyExist

from application.exceptions.services import InteractorError


class RegistrationInteractor(InteractorInterface):
    def __init__(self, user_service: UserServiceInterface,
                 auth_service: UserServiceInterface):
        self.user_service = user_service
        self.auth_service = auth_service

    async def execute(self, user_data: User) -> User:
        try:
            user_uuid = await self.auth_service.register(user_data)
            user_with_id = UserWithId(**user_data.to_dict(), id=user_uuid)
            db_user = await self.user_service.register(user_with_id)
            return db_user

        except AlreadyExist as ae:
            raise AlreadyExist(
                f"User service failed saving the user. Original error {str(ae)}"
            ) from ae

        except RegistrationError as re:
            raise InteractorError(
                f"Registration event could not be completed in the UserService. Original error f{str(re)}"
            ) from re
