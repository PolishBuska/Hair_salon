from domain.interfaces.services.user import UserServiceInterface
from domain.interfaces.interactor import InteractorInterface
from domain.models.user import User, UserWithId


class RegistrationInteractor(InteractorInterface):
    def __init__(self, user_service: UserServiceInterface,
                 auth_service: UserServiceInterface):
        self.user_service = user_service
        self.auth_service = auth_service

    async def execute(self, user_data: User) -> User:
        user_uuid = await self.auth_service.register(user_data)
        user_with_id = UserWithId(**user_data.to_dict(), id=user_uuid)
        db_user = await self.user_service.register(user_with_id)
        return db_user
