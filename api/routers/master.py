from injector import inject
from fastapi import APIRouter, Depends

from infrastructure.dependency import get_repository
from infrastructure.models import Service

from application.services.master import MasterService

from domain.interfaces.repositories.master import MasterRepositoryInterface

from api.schemas.master import ServiceCreate

router = APIRouter(

)


@router.post('/services')
@inject
async def create_service(
                         service_data: ServiceCreate,
                         repo=Depends(get_repository(model=Service, repo=MasterRepositoryInterface)),
                         ):
    service = MasterService(repo=repo)
    result = await service.create_service(data=service_data)
    return result


@router.get('/services')
@inject
async def get_services():
    ...


@router.get('/services/{service_id}')
async def get_service(service_id: int):
    ...
