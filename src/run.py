from datetime import datetime

from src.app.domain.base.value_object import Id
from src.app.domain.user.enums import UserRole
from src.app.domain.user.vo_user import UserEmail, UserName, UserFullname
from src.app.domain.user_auth.entity_user_auth import UserAuth
from src.app.domain.user_auth.vo_user_auth import UserPasswordHash, UserCreatedAt, UserUpdateAt
from src.app.main.app_factory import create_app

kwargs = {
    "id_": 12,
    "email": "user@example.com",
    "username": "john_doe",
    "full_name": "John Doe",
    "role": "admin",
    "is_active": True,
    "password": "hashed_password",
    "created_at": datetime.now(),
    "updated_at": datetime.now()
}

user_auth = UserAuth(
    id_=Id(1),
    email=UserEmail("4141d1@gmail.com"),
    username=UserName("jf2f3"),
    full_name=UserFullname("Vasa Pupkin"),
    role=UserRole.ADMIN,
    is_active=True,
    password=UserPasswordHash("fb2tbubuffwjg"),
    created_at=UserCreatedAt(datetime.now()),
    updated_at=UserUpdateAt(datetime.now())
)
print(user_auth)
new_user = user_auth.create_user(**kwargs)
print(new_user)
