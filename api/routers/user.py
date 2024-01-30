from fastapi import APIRouter, Depends
from injector import inject


from api.schemas.user import UserCreated

from application.services.user import UserService

from infrastructure.dependency import get_repository
from infrastructure.models import User
from infrastructure.repositories.user import UserRepository

router = APIRouter(

)


@router.post('/sign-on')
async def registration(data: UserCreated,
                       repo=Depends(get_repository(repo=UserRepository, model=User))):
    service = UserService(repo=repo)
    result = await service.register(data=data)
    return result
