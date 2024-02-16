
from fastapi import APIRouter, HTTPException, status, Depends

from api.schemas.user import UserCreated, UserReturned

from application.dto.user import UserDTO

from domain.exceptions.user import AlreadyExist
from domain.interfaces.services.user import UserServiceInterface
from domain.models.user import User

from infrastructure.dependency import user_service_stub

router = APIRouter(

)


@router.post('/sign-on')
async def registration(data: UserCreated,
                       user_service: UserServiceInterface = Depends(user_service_stub)
                       ):
    try:
        data = data.model_dump()
        user_data = User(**data)
        result = await user_service.register(user_data)
        return result
    except AlreadyExist as ae:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exist"
        ) from ae
