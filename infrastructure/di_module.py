# infrastructure/di_modules.py
from injector import Binder, Module, singleton

from domain.interfaces.repositories.master import MasterRepositoryInterface
from domain.interfaces.repositories.general import GenericRepositoryInterface
from domain.interfaces.repositories.user import UserRepositoryInterface

from infrastructure.repositories.master import MasterRepository
from infrastructure.repositories.general import GenericRepository
from infrastructure.repositories.user import UserRepository


class MasterRepositoryModule(Module):
    def configure(self, binder: Binder):
        binder.bind(MasterRepositoryInterface, to=MasterRepository, scope=singleton)


class GenericRepositoryModule(Module):
    def configure(self, binder: Binder):
        binder.bind(GenericRepositoryInterface, to=GenericRepository, scope=singleton)


class UserRepositoryModule(Module):
    def configure(self, binder: Binder):
        binder.bind(UserRepositoryInterface, to=UserRepository, scope=singleton)
