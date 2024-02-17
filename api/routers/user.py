
from fastapi import APIRouter, HTTPException, status, Depends

from api.schemas.user import UserCreated


from domain.exceptions.user import AlreadyExist
from domain.models.user import User
from domain.interfaces.interactor import InteractorInterface

from infrastructure.dependency import reg_interactor_stub

router = APIRouter(

)


@router.post('/sign-on')
async def registration(data: UserCreated,
                       user_interactor: InteractorInterface = Depends(reg_interactor_stub),

                       ):
    try:
        data = data.model_dump()
        user_data = User(**data)
        result = await user_interactor.execute(user_data)
        return result
    except AlreadyExist as ae:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exist"
        ) from ae
