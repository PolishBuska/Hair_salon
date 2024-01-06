from domain.interfaces.repositories.general import GenericRepositoryInterface


class MasterService:
    def __init__(self, repo: GenericRepositoryInterface):
        self._repo = repo

    async def create_service(self, data):
        result = await self._repo.create(data=data)

        return result

    async def assign_timing_to_service(self):
        ...

    async def map_service_timing_to_schedule(self):
        ...

