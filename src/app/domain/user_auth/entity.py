from dataclasses import dataclass, fields, asdict
from datetime import datetime
from typing import List
from uuid import UUID


from app.domain.base.entity import Entity
from app.domain.base.value_object import Id
from app.domain.user.entity import User
from app.domain.user_auth.ports.password_hasher import PasswordHasher
from app.domain.user_auth.ports.timestamp_manager import TimestampManager
from app.domain.user_auth.value_object import UserPasswordHash, UserCreatedAt, UserUpdateAt, RawPassword


@dataclass(eq=False, kw_only=True)
class UserAuth(User):
    password: UserPasswordHash
    created_at: UserCreatedAt
    updated_at: UserUpdateAt


    def create(
        self,
        raw_password: RawPassword,
        password_hasher: PasswordHasher, timestamp_manager: TimestampManager,
        user: User
    ) -> UserAuth:
        password_hash: UserPasswordHash = UserPasswordHash(password_hasher.hash(raw_password))
        created_at: UserCreatedAt = UserCreatedAt(timestamp_manager.current_time())
        updated_at: UserUpdateAt = UserUpdateAt(timestamp_manager.current_time())
        return UserAuth(
            password=password_hash,
            created_at=created_at,
            updated_at=updated_at,
            **asdict(user)
        )


    def is_password_valid(self, raw_password: RawPassword, password_hasher: PasswordHasher) -> bool:
        return password_hasher.verify_password(
            raw_password=raw_password,
            hashed_password=self.password.value
        )


    def change_password(self, raw_password: RawPassword, password_hasher: PasswordHasher) -> None:
        new_hashed_password: UserPasswordHash = UserPasswordHash(password_hasher.hash(raw_password))
        self.password = new_hashed_password


    # def create_user(self, **kwargs):
    #     # IDGenetaror
    #     # HashPassword
    #     self.validate_kwargs(**kwargs)
    #     return UserAuth(**kwargs)
    #
    #
    #
    # def get_required_fields(self):
    #     """
    #     Cre
    #     """
    #     return [field.name for field in fields(self)]
    #
    #
    # def validate_kwargs(self, **kwargs):
    #     """
    #     Validates that 'instance_kwargs' contains all required keys
    #
    #     :param kwargs: The dictionary to validate.
    #     :raises ValueError: If incorrect size of received kwargs or missing requiring keys.
    #     """
    #     required_keys = self.get_required_fields()
    #     len_required_keys = len(required_keys)
    #
    #
    #     if len_required_keys != len(kwargs):
    #         raise ValueError(f"Size of required keys must be - {len_required_keys}. Got {len(kwargs)}")
    #
    #
    #     missing_keys = list((key for key in required_keys if key not in kwargs))
    #     if missing_keys:
    #         raise ValueError(f"Missing requiring keys - {missing_keys}")
