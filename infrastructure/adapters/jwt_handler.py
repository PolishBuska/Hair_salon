
from datetime import datetime, timedelta

from jose import JWTError, jwt

from config import get_config

from api.schemas.jwt import TokenPayLoad


class AuthProvider:
    config = get_config()
    SECRET_KEY = config.secret_key
    ALGORITHM = config.algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES = config.access_token_expire_minutes
    oauth2_scheme = config.oauth2_scheme

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


def auth_provider_factory():
    return AuthProvider()
