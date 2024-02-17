from abc import ABC, abstractmethod


class GenericRepositoryInterface(ABC):

    @abstractmethod
    async def create(self, data: dict) -> dict | None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, *args, **kwargs) -> dict | None:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, pk: int):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, pk):
        raise NotImplementedError
