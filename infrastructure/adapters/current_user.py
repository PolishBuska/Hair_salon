from fastapi import Depends, HTTPException, status
from jose import JWTError

from application.dto.user import CurrentUserDTO
from config import get_config
from infrastructure.dependency import get_repository
from infrastructure.models import User
from infrastructure.repositories.general import GenericRepository


async def get_current_user(self,
                           token: str = Depends(get_config().oauth2_scheme),
                           repo=Depends(get_repository(model=User,
                                                       repo=GenericRepository))):
    try:
        credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                              detail=f'Could not validate credentials',
                                              headers={"WWW-Authenticate": "Bearer"})
        token_verified = await self.verify_access_token(token, credentials_exception)
        user = await repo.find_one(pk=token_verified.user_id)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Could not validate credentials',
                            headers={"WWW-Authenticate": "Bearer"})
    return CurrentUserDTO(user_id=user.id, role_id=user.role_id)
