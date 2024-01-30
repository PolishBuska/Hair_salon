from sqlalchemy.exc import IntegrityError

from domain.exceptions.master import MasterServiceException, ServiceAlreadyExist
from domain.interfaces.repositories.master import MasterRepositoryInterface

from api.schemas.master import ServiceCreate

from infrastructure.loggers.container import LoggerContainer


class MasterService:
    def __init__(self, repo: MasterRepositoryInterface):
        self._repo = repo
        self._logger = LoggerContainer()

    async def create_service(self, data: ServiceCreate):
        try:
            result = await self._repo.create(data=data.model_dump())
            return result
        except IntegrityError as ie:
            logger = self._logger.get_logger(name="WARNING")
            logger.msg(message=f"{str(ie)}")
            raise ServiceAlreadyExist(f"the service {data.name} already exist") from ie
        except Exception as e:
            logger = self._logger.get_logger(name="CRITICAL")
            logger.msg(message=f"{str(e)}")
            raise MasterServiceException(
                f"something went wrong with the creation of service event. Original error {str(e)}"
                                ) from e

    async def assign_timing_to_service(self):
        ...

    async def map_service_timing_to_schedule(self):
        ...

