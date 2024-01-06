from pydantic import BaseModel


class TokenPayLoad(BaseModel):
    user_id: int
    role_id: int
