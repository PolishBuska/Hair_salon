
class UserDTO:
    _role_id: int
    _email: str
    _password: str
    _nickname: str

    def __init__(self, **kwargs):
        self._uuid = kwargs.get('id')
        self._role_id = kwargs.get('role_id')
        self._email = kwargs.get('email')
        self._password = kwargs.get('password')
        self._nickname = kwargs.get('nickname')

    @property
    def uuid(self) -> str:
        """
        Return the user uuid.
        """
        return self._uuid

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

    def __init__(self, user_id: str, role: str, email: str, email_verified: bool, username: str):
        """
        Initialize CurrentUserDTO with user data.
        """
        self._user_id = user_id
        self._role = role
        self._email = email
        self._email_verified = email_verified
        self._username = username

    @property
    def user_id(self) -> str:
        """
        Return the user ID.
        """
        return self._user_id

    @property
    def role(self) -> str:
        """
        Return the user's role.
        """
        return self._role

    @property
    def email(self) -> str:
        """
        Return the user's email.
        """
        return self._email

    @property
    def email_verified(self) -> bool:
        """
        Return whether the email is verified.
        """
        return self._email_verified

    @property
    def username(self) -> str:
        """
        Return the preferred username.
        """
        return self._username

    def to_dict(self) -> dict:
        """
        Convert the DTO to a dictionary.
        """
        return {
            'user_id': self.user_id,
            'role': self.role,
            'email': self.email,
            'email_verified': self.email_verified,
            'username': self.username,
        }
