from typing import Annotated
import re

from pydantic import BaseModel, Field, field_validator
from pydantic.types import Decimal, constr


class ServiceBase(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=25,
    )
    price: Decimal = Field(
        ...,
        gt=0.000,
        decimal_places=0,
        max_digits=100,

    )
    description: Annotated[str, constr(min_length=15, max_length=400)]

    @field_validator('name')
    def check_name(cls, v):
        if not re.search('[a-zA-Z]', v):
            raise ValueError('Name must contain at least one literal')
        if re.search('[#$%^&*(!)@]', v):
            raise ValueError('Name cannot contain special characters')
        return v


class ServiceReturn(ServiceBase):
    id: int


class ServiceCreate(ServiceBase):
    ...
