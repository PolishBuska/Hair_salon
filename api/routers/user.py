from fastapi import APIRouter, Depends, HTTPException, status


from api.schemas.user import UserCreated, UserReturned

from application.services.user import UserService
from application.dto.user import UserDTO

from domain.exceptions.user import AlreadyExist

from infrastructure.dependency import get_repository
from infrastructure.models import User
from infrastructure.repositories.user import UserRepository

router = APIRouter(

)


@router.post('/sign-on', response_model=UserReturned)
async def registration(data: UserCreated,
                       repo=Depends(get_repository(repo=UserRepository, model=User))):
    try:
        data = data.model_dump()
        user_data = UserDTO(**data)
        service = UserService(repo=repo)
        result = await service.register(data=user_data)
        return result
    except AlreadyExist as ae:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exist"
        ) from ae
