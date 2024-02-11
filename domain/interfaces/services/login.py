from abc import ABC, abstractmethod

from domain.models.login import LoginCreds


class LoginServiceInterface(ABC):

    @abstractmethod
    async def login(self, creds: LoginCreds):
        raise NotImplementedError
