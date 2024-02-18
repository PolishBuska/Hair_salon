from abc import ABC, abstractmethod

from core.models.user import UserCreds


class LoginServiceInterface(ABC):

    @abstractmethod
    async def login(self, creds: UserCreds):
        raise NotImplementedError
