from sqlalchemy.exc import IntegrityError

from core.exceptions.master import MasterServiceException, ServiceAlreadyExist
from core.interfaces.repositories.master import MasterRepositoryInterface
from core.models.pagination import Pagination
from core.models.service import Services

from infrastructure.loggers.container import LoggerContainer

from application.dto.user import CurrentUserDTO


class MasterService:
    def __init__(self, repo: MasterRepositoryInterface):
        self._repo = repo
        self._logger = LoggerContainer()

    async def create_service(self, data: dict, current_user: CurrentUserDTO):
        try:
            data['user_id'] = current_user.user_id
            result = await self._repo.create(data=data)
            return result
        except IntegrityError as ie:
            logger = self._logger.get_logger(name="WARNING")
            logger.msg(message=f"{str(ie)}")
            raise ServiceAlreadyExist(f"the service {data['name']} already exist") from ie
        except Exception as e:
            logger = self._logger.get_logger(name="CRITICAL")
            logger.msg(message=f"{str(e)}")
            raise MasterServiceException(
                f"something went wrong with the creation of service event. Original error {str(e)}"
                                ) from e

    async def get_services_by_master(self, pagination: Pagination, pk: int) -> Services:
        try:
            result = await self._repo.get_services_by_master(pk=pk, pagination=pagination)
            result = Services(services=result)
            return result
        except Exception as e:
            logger = self._logger.get_logger(name="CRITICAL")
            logger.msg(message=f"{str(e)}")
            raise MasterServiceException(
                f"something went wrong with the getting of services event. Original error {str(e)}"
                                ) from e

    async def assign_timing_to_service(self):
        ...

    async def map_service_timing_to_schedule(self):
        ...

