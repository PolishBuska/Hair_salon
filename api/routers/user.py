from fastapi import APIRouter, Depends
from injector import inject

from domain.interfaces.repositories.user import UserRepositoryInterface

from api.schemas.user import UserCreated

from application.services.user import UserService

from infrastructure.dependency import get_repository
from infrastructure.models import User

router = APIRouter(

)


@router.post('/sign-on')
@inject
async def registration(data: UserCreated,
                       repo=Depends(get_repository(repo=UserRepositoryInterface, model=User))):
    service = UserService(repo=repo)
    result = await service.register(data=data)
    return result
