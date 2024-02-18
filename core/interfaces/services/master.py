from abc import ABC, abstractmethod


class MasterServiceInterface(ABC):
    """
        This class shows the general methods of a master instance
    """
    @abstractmethod
    async def create_service(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get_services_by_master(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def assign_timing_to_service(self):
        raise NotImplementedError

    @abstractmethod
    async def map_service_timing_to_schedule(self):
        raise NotImplementedError


