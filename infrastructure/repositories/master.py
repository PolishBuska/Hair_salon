from sqlalchemy import select, insert

from core.models.pagination import Pagination
from core.exceptions.master import NotFoundServicesByMaster

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
        res = res.unique().scalars().all()
        if not res:
            raise NotFoundServicesByMaster(f"Services weren't found")
        return res



