from dataclasses import dataclass


@dataclass
class BaseUser:
    email: str
    nickname: str
    role_id: int

    def to_dict(self):
        return {
            'email': self.email,
            'nickname': self.nickname,
            'role_id': self.role_id,
        }


@dataclass
class User(BaseUser):
    password: str

    def to_dict(self):
        return {
            'email': self.email,
            'nickname': self.nickname,
            'role_id': self.role_id,
        }


@dataclass
class UserWithId(BaseUser):
    id: str

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'nickname': self.nickname,
            'role_id': self.role_id,
        }
