from abc import ABC, abstractmethod


class MasterServiceInterface(ABC):
    """
        This class shows the general methods of a master instance
    """

    @abstractmethod
    async def set_date(self):
        raise NotImplementedError

    @abstractmethod
    async def approve_date(self):
        raise NotImplementedError

