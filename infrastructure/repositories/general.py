from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, update, select


class GenericRepository:
    def __init__(self, model, session: AsyncSession):
        self.model = model
        self.session = session

    async def create(self, data: dict) -> dict | None:
        stmt = insert(self.model).values(data).returning(self.model)
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar()

    async def update(self, pk: int, data: dict) -> dict | None:
        stmt = update(self.model).values(data).where(self.model.id == pk).returning(self.model.id)
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar()

    async def get_all(
            self,
            limit: int,
            offset: int,
            search: str,
                      ):
        query = (select(self.model).
                 filter(
            self.model.title.contains(search)).
                 limit(
            limit).
                 offset(offset)
                 )
        res = await self.session.execute(query)
        return res.unique().scalars().all()

    async def get_one(self, pk: int):
        query = select(self.model).where(self.model.id == pk)
        res = await self.session.execute(query)
        return res.scalar()

    async def delete(self, pk: int):
        stmt = update(self.model).values(status=False).where(self.model.id == pk)
        await self.session.execute(stmt)

