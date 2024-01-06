from sqlalchemy import select, update
from infrastructure.repositories.general import GenericRepository

from domain.interfaces.repositories.user import UserRepositoryInterface


class UserRepository(GenericRepository, UserRepositoryInterface):

    async def get_user(self, pk: int):
        result = await super().get_one(pk=pk)
        return result

    async def get_all_users(self, search, limit, offset):
        result = await super().get_all(search=search,
                                       limit=limit,
                                       offset=offset)
        return result

    async def add_user(self, data: dict) -> dict | None:
        result = await super().create(data=data)
        return result

    async def disable_user(self, pk: int):
        result = update(self.model).where(self.model.id == pk).values(status=False).returning(self.model.id)
        return result

    async def find_one_by_email(self, email: str):
        query = select(self.model).where(self.model.email == email)

        res = await self.session.execute(query)
        return res.scalar()
