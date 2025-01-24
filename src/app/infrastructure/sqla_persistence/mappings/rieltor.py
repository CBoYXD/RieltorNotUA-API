from sqlalchemy import UUID, Column, String, Table, Integer, ForeignKey
from sqlalchemy.orm import composite

from app.domain.base.value_object import Id
from app.domain.rieltor.entity import Rieltor
from app.domain.rieltor.value_object import RieltorAgencyName, RieltorLicenseNumber, RieltorExperienceYears
from app.infrastructure.sqla_persistence.orm_registry import mapping_registry
from app.infrastructure.sqla_persistence.mappings.user import users_table


rieltors_table = Table(
    "rieltors",
    mapping_registry.metadata,
    Column("id", UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True),
    Column("agency_name", String, nullable=False),
    Column("license_number", Integer, nullable=False, unique=True),
    Column("experience_years", Integer, nullable=False),
)


def map_rieltors_table() -> None:
    mapping_registry.map_imperatively(
        Rieltor,
        rieltors_table,
        properties={
            "id_": composite(Id, rieltors_table.c.id),
            "agency_name": composite(RieltorAgencyName, rieltors_table.c.agency_name),
            "license_number": composite(RieltorLicenseNumber, rieltors_table.c.license_number),
            "experience_years": composite(RieltorExperienceYears, rieltors_table.c.experience_years),
        },
        column_prefix="_",
        polymorphic_on=users_table.c.role,
        polymorphic_identity="rieltor"
    )
