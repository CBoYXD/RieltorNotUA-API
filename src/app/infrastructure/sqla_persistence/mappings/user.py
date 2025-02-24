from sqlalchemy import UUID, Boolean, Column, Enum, String, Table
from sqlalchemy.orm import composite

from app.domain.base.value_object import Id
from app.domain.user.entity import User
from app.domain.user.enums import UserRole
from app.domain.user.validation.constants import USERNAME_MAX_LEN, FULLNAME_MAX_LEN
from app.domain.user.value_object import UserName, UserEmail, UserFullname
from app.infrastructure.sqla_persistence.orm_registry import mapping_registry

users_table = Table(
    "users",
    mapping_registry.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True),
    Column("email", String, nullable=False, unique=True),
    Column("username", String(USERNAME_MAX_LEN), nullable=False, unique=True), 
    Column("full_name", String(FULLNAME_MAX_LEN), nullable=False),
    Column(
        "role",
        Enum(UserRole),
        default=UserRole.USER,
        nullable=False,
    ),
    Column("is_active", Boolean, default=True, nullable=False),
)

user_properties = {
    "id_": composite(Id, users_table.c.id),
    "email": composite(UserEmail, users_table.c.email),
    "username": composite(UserName, users_table.c.username),
    "full_name": composite(UserFullname, users_table.c.full_name),
    "role": users_table.c.role,
    "is_active": users_table.c.is_active,
}

def map_users_table() -> None:
    mapping_registry.map_imperatively(
        User,
        users_table,
        properties=user_properties,
        column_prefix="_",
        polymorphic_on=users_table.c.role,
        polymorphic_identity="user"
    )
