from injector import inject
from fastapi import APIRouter, Depends, HTTPException, status

from infrastructure.loggers.container import LoggerContainer
from infrastructure.jwt_handler import AuthProvider
from infrastructure.dependency import master_service_stub

from application.dto.user import CurrentUserDTO

from domain.exceptions.master import ServiceAlreadyExist, MasterServiceException
from domain.interfaces.services.master import MasterServiceInterface

from api.schemas.master import ServiceCreate


router = APIRouter(

)


@router.post('/services')
async def create_service(
                         service_data: ServiceCreate,
                         master_service: MasterServiceInterface = Depends(master_service_stub),
                         current_user: CurrentUserDTO = Depends(AuthProvider().get_current_user),

):
    logger = LoggerContainer()
    try:
        data = service_data.model_dump()
        result = await master_service.create_service(
            data=data,
            current_user=current_user
        )
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

