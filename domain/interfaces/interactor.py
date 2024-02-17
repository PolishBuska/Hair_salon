from abc import ABC, abstractmethod


class InteractorInterface(ABC):

    @abstractmethod
    async def execute(self, *args, **kwargs):
        raise NotImplementedError
