import re
from enum import Enum
from typing import Annotated

from pydantic import BaseModel, EmailStr, constr, Field, field_validator


class Roles(int, Enum):
    Customer = 1
    Master = 2
    Admin = 3


class UserBase(BaseModel):
    username: Annotated[str, constr(min_length=5, max_length=50)]
    email: Annotated[EmailStr, constr(max_length=50, min_length=10)]
    role_id: Roles


class UserReturned(UserBase):
    id: int


class UserCreated(UserBase):
    password: str = Field(..., min_length=5, max_length=25)

    @field_validator('password')
    def validate_password(cls, v):
        if not re.search('[a-zA-Z]', v):
            raise ValueError('Password must contain at least one literal')
        if re.search('[#$%^&*(!)@]', v):
            raise ValueError('Password cannot contain special characters')
        return v
