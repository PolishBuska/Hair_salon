
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database import Database


def get_repository(model, repo):
    def _get_generic_repository(session: AsyncSession = Depends(Database().get_session)):
        return repo(model, session)

    return _get_generic_repository
