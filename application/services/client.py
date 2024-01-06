from domain.interfaces.services.client import ClientServiceInterface
from infrastructure.repositories.general import GenericRepository


class ClientService(ClientServiceInterface):

    def __init__(self,
                 repo: GenericRepository,
                 ):
        self._repo = repo

    async def get_date(self, pk: int):
        query = await self._repo.get_one(pk=pk)
        return query

    async def get_dates(self):
        query = await self._repo.get_all()
        return query
