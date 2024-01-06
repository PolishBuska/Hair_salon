
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from config import get_config


class Database:
    def __init__(self):
        self._config = get_config()
        self._engine = create_async_engine(url=self._config.db_url)

        self._async_session_factory = async_sessionmaker(
            self._engine, expire_on_commit=False
        )

    async def get_session(self):
        async with self._async_session_factory() as session:
            yield session

    async def get_engine(self):
        return self._engine


def get_base():
    _base = declarative_base()
    return _base
