from dataclasses import dataclass, fields
from datetime import datetime
from typing import List

from src.app.domain.user.entity_user import User
from src.app.domain.user_auth.vo_user_auth import UserPasswordHash, UserCreatedAt, UserUpdateAt


@dataclass(eq=False, kw_only=True)
class UserAuth(User):
    password: UserPasswordHash
    created_at: UserCreatedAt
    updated_at: UserUpdateAt


    def create_user(self, **kwargs):
        # HashPassword
        self.validate_kwargs(**kwargs)
        return UserAuth(**kwargs)



    def get_required_fields(self):
        """
        Cre
        """
        return [field.name for field in fields(self)]


    def validate_kwargs(self, **kwargs):
        """
        Validates that 'instance_kwargs' contains all required keys

        :param kwargs: The dictionary to validate.
        :raises ValueError: If incorrect size of received kwargs or missing requiring keys.
        """
        required_keys = self.get_required_fields()
        len_required_keys = len(required_keys)


        if len_required_keys != len(kwargs):
            raise ValueError(f"Size of required keys must be - {len_required_keys}. Got {len(kwargs)}")


        missing_keys = list((key for key in required_keys if key not in kwargs))
        if missing_keys:
            raise ValueError(f"Missing requiring keys - {missing_keys}")
