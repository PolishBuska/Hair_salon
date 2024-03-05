from sqlalchemy import select

from core.models.pagination import Pagination
from infrastructure.repositories.general import GenericRepository


class MasterRepository(GenericRepository):
    async def get_services_by_master(self, pk: str, pagination: Pagination):
        query = (select(self.model).where(self.model.user_id == str(pk)).
                 filter(
            self.model.name.contains(pagination.search)).
                 limit(
             pagination.limit).
                 offset(pagination.offset)
                 )
        res = await self.session.execute(query)
        return res.unique().scalars().all()

