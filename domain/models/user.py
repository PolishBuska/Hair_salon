from dataclasses import dataclass


@dataclass
class User:
    email: str
    nickname: str
    password: str
    role_id: int
    enabled: bool = True

