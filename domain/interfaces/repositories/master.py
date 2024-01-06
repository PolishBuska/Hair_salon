from abc import ABC

from domain.interfaces.repositories.general import GenericRepositoryInterface


class MasterRepositoryInterface(GenericRepositoryInterface,
                                ABC):
    ...

