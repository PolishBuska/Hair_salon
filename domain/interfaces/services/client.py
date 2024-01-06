from abc import ABC, abstractmethod


class ClientServiceInterface(ABC):
    """
        This class shows the general methods of a client instance
    """

    @abstractmethod
    async def get_dates(self):
        raise NotImplementedError

    @abstractmethod
    async def get_date(self, pk: int):
        raise NotImplementedError
