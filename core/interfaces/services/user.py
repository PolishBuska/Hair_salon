from abc import ABC, abstractmethod


class UserServiceInterface(ABC):
    @abstractmethod
    async def register(self, *args, **kwargs):
        raise NotImplementedError
