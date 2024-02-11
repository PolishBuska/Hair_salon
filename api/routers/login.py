from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from domain.exceptions.user import AuthServiceError
from domain.interfaces.services.login import LoginServiceInterface
from domain.models.login import LoginCreds

from infrastructure.dependency import login_service_stub

router = APIRouter()


@router.post('/login')
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(),
                service: LoginServiceInterface = Depends(login_service_stub)):
    try:
        if not user_credentials:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No data provided")

        token = await service.login(
            creds=LoginCreds(
                user_credentials.username, user_credentials.password
            )
        )
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Wrong credentials")
        return token
    except AuthServiceError:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Currently not available")

