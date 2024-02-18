from abc import ABC, abstractmethod


class AdminServiceInterface(ABC):
    """
        This class shows the general methods of an admin instance
    """

    @abstractmethod
    async def add_service(self):
        raise NotImplementedError

    @abstractmethod
    async def remove_service(self):
        raise NotImplementedError
