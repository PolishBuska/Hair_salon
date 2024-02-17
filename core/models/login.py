from dataclasses import dataclass


@dataclass
class LoginCreds:
    username: str
    plain_password: str

