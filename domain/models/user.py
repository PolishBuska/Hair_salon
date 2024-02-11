from dataclasses import dataclass

from domain.models.user_id import UserId


@dataclass
class User:
    id: UserId
    nickname: str
