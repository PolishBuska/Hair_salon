from injector import inject
from fastapi import APIRouter, Depends, HTTPException, status

from infrastructure.dependency import get_repository
from infrastructure.models import Service
from infrastructure.loggers.container import LoggerContainer

from application.services.master import MasterService

from domain.interfaces.repositories.master import MasterRepositoryInterface
from domain.exceptions.master import ServiceAlreadyExist, MasterServiceException

from api.schemas.master import ServiceCreate

router = APIRouter(

)


@router.post('/services')
@inject
async def create_service(
                         service_data: ServiceCreate,
                         repo=Depends(get_repository(model=Service, repo=MasterRepositoryInterface)),
                         logger=LoggerContainer()
                         ):
    try:
        service = MasterService(repo=repo)
        result = await service.create_service(data=service_data)
        return result
    except ServiceAlreadyExist as aee:
        logger.get_logger("WARNING").msg(message=f"{str(aee)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(aee)) from aee
    except MasterServiceException as mse:
        logger.get_logger("WARNING").msg(message=f"{str(mse)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Could not process") from mse


@router.get('/services')
@inject
async def get_services():
    ...


@router.get('/services/{service_id}')
async def get_service(service_id: int):
    ...
