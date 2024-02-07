
class UserDTO:
    _role_id: int
    _email: str
    _password: str
    _nickname: str

    def __init__(self, **kwargs):
        self._role_id = kwargs.get('role_id')
        self._email = kwargs.get('email')
        self._password = kwargs.get('password')
        self._nickname = kwargs.get('nickname')

    @property
    def nickname(self) -> str:
        """
        Return the user nickname.
        """
        return self._nickname

    @property
    def password(self) -> str:
        """
        Return the user password.
        """
        return self._password

    def set_password(self, new_password: str):
        self._password = new_password

    @property
    def email(self) -> str:
        """
        Return the user email.
        """
        return self._email

    @property
    def role_id(self) -> int:
        """
        Return the role id.
        """
        return self._role_id

    def to_dict(self) -> dict:
        """
        Convert the DTO to a dictionary.
        """
        return {
            'role_id': self.role_id,
            'email': self.email,
            'password': self.password,
            'nickname': self.nickname,
        }


class CurrentUserDTO:
    """
    Data Transfer Object for current user data.
    """
    _user_id: int
    _role_id: int

    def __init__(self, user_id: int, role_id: int):
        """
        Initialize CurrentUserDTO with user id and role id.
        """
        self._user_id = user_id
        self._role_id = role_id

    @property
    def user_id(self) -> int:
        """
        Return the user id.
        """
        return self._user_id

    @property
    def role_id(self) -> int:
        """
        Return the role id.
        """
        return self._role_id

    def to_dict(self) -> dict:
        """
        Convert the DTO to a dictionary.
        """
        return {
            'role_id': self.role_id,
            'user_id': self.user_id,
        }
