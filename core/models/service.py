from dataclasses import dataclass
from decimal import Decimal
import datetime as dt
from typing import List

from core.models.user_id import UserId


@dataclass
class Service:
    user_id: UserId
    id: int
    name: str
    price: Decimal
    description: str
    created_at: dt.datetime.utcnow()


@dataclass
class Services:
    services: List[Service]
