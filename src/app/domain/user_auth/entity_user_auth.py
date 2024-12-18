from dataclasses import dataclass, fields
from datetime import datetime
from typing import List
from uuid import UUID


from src.app.domain.base.entity import Entity
from src.app.domain.base.value_object import Id
from src.app.domain.user.entity_user import User
from src.app.domain.user_auth.ports.password_hasher import PasswordHasher
from src.app.domain.user_auth.ports.timestamp_manager import TimestampManager
from src.app.domain.user_auth.vo_user_auth import UserPasswordHash, UserCreatedAt, UserUpdateAt, RawPassword


@dataclass(eq=False, kw_only=True)
class UserAuth(Entity[Id]):
    password: UserPasswordHash # ???
    created_at: UserCreatedAt
    updated_at: UserUpdateAt
    user: User


    def create_user(
            self,
            raw_password: RawPassword,
            password_hasher: PasswordHasher, timestamp_manager: TimestampManager,
    ):
        # user_id = user_id_generator() or made right factory for id TODO
        password_hash: UserPasswordHash = UserPasswordHash(password_hasher.hash(raw_password))
        created_at: UserCreatedAt = UserCreatedAt(timestamp_manager.current_time())
        updated_at: UserUpdateAt = UserUpdateAt(None)
        user: User = None # TODO
        return UserAuth(
            id_= "18418ydh1bdc97t4y1dbc3r1bcb937y5", #TODO
            password=password_hash,
            created_at=created_at,
            updated_at=updated_at,
            user=user
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
