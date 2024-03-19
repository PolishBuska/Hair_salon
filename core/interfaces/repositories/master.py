from abc import ABC, abstractmethod

from core.interfaces.repositories.general import GenericRepositoryInterface


class MasterRepositoryInterface(GenericRepositoryInterface,
                                ABC):
    @abstractmethod
    async def get_services_by_master(self, *args, **kwargs):
        raise NotImplementedError
