from sqlalchemy import select

from core.models.pagination import Pagination
from infrastructure.repositories.general import GenericRepository


class MasterRepository(GenericRepository):
    async def get_services_by_master(self, pk: int, pagination: Pagination):
        query = (select(self.model).where(self.model.id == pk).
                 filter(
            self.model.name.contains(pagination.search)).
                 limit(
             pagination.limit).
                 offset(pagination.offset)
                 )
        res = await self.session.execute(query)
        return res.unique().scalars().all()

