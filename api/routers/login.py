from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from core.exceptions.user import AuthServiceError
from core.interfaces.services.login import LoginServiceInterface
from core.models.user import UserCreds

from infrastructure.dependency import login_service_stub

router = APIRouter()


@router.post('/login')
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(),
                service: LoginServiceInterface = Depends(login_service_stub)):
    try:
        if not user_credentials:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No data provided")

        token = await service.login(
            UserCreds(
                user_credentials.username, user_credentials.password
            )
        )
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Wrong credentials")
        response = JSONResponse({'message': 'success'})
        response.set_cookie(key='access_token', value=token, httponly=True, samesite='strict', secure=True)
        return response
    except AuthServiceError:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Currently not available")

