# pylint: disable=C0301 (line-too-long)

import base64
import hashlib
import hmac

import bcrypt

from app.domain.user_auth.value_object import UserPasswordHash
from app.domain.user_auth.ports.password_hasher import PasswordHasher
from passlib.context import CryptContext


class BcryptPasswordHasher(PasswordHasher):
    def __init__(self, context: CryptContext):
        self._context = context

    def hash(self, raw_password: str) -> str:
        return self._context.hash(raw_password.value)

    def verify(self, raw_password: str, hashed_password: UserPasswordHash) -> bool:
        return self._context.verify(raw_password, hashed_password.value)
