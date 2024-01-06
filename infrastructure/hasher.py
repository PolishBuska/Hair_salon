"""store your not domain related utils here"""
from passlib.context import CryptContext


class PwdContext:
    """Simple definer, specify this through composition"""

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

