from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):
    @abstractmethod
    async def find_one_by_email(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_user(self, pk: int):
        raise NotImplementedError

    @abstractmethod
    async def add_user(self, data):
        raise NotImplementedError

    @abstractmethod
    async def get_all_users(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def disable_user(self, pk):
        raise NotImplementedError

