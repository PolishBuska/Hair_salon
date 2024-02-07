from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from domain.exceptions.user import AuthServiceError

from application.services.login import LoginService

from infrastructure.models import User
from infrastructure.dependency import get_repository


from infrastructure.repositories.user import UserRepository

router = APIRouter()


@router.post('/login')
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(),
                repo=Depends(get_repository(model=User,
                                            repo=UserRepository))):
    try:
        if not user_credentials:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No data provided")
        service = LoginService(plain_password=user_credentials.password,
                               email=user_credentials.username,
                               repo=repo)
        token = await service.login()
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Wrong credentials")
        return token
    except AuthServiceError:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Currently not available")

