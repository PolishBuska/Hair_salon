
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt

from starlette import status

from injector import inject

from config import get_config

from infrastructure.dependency import get_repository
from infrastructure.models import User

from api.schemas.jwt import TokenPayLoad

from domain.interfaces.repositories.general import GenericRepositoryInterface


class AuthProvider:
    config = get_config()
    SECRET_KEY = config.secret_key
    ALGORITHM = config.algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES = config.access_token_expire_minutes
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/v2/login')

    async def create_access_token(self,
                                  data: dict):
        if not isinstance(data, dict):
            raise ValueError("Invalid input data")
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)

        return encoded_jwt

    async def verify_access_token(self,
                                  token: str,
                                  credentials_exception):
        try:
            payload = jwt.decode(token,
                                 self.SECRET_KEY,
                                 algorithms=[self.ALGORITHM])
            user_id = payload.get("user_id")
            role_id = payload.get("role_id")

            token_data = TokenPayLoad(user_id=user_id,
                                      role_id=role_id)
        except JWTError:
            raise credentials_exception
        return token_data

    @inject
    async def get_current_user(self,
                               token: str = Depends(oauth2_scheme),
                               repo=Depends(get_repository(model=User,
                                                           repo=GenericRepositoryInterface))):
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
        return user
