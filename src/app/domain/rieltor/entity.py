from dataclasses import dataclass, asdict

from app.domain.rieltor.value_object import (
    RieltorAgencyName,
    RieltorExperienceYears,
    RieltorLicenseNumber,
)
from app.domain.user.entity import User
from app.domain.base.ports.uuid_generator import UUIDGenerator


@dataclass(eq=False, kw_only=True)
class Rieltor(User):
    agency_name: RieltorAgencyName
    license_number: RieltorLicenseNumber
    experience_years: RieltorExperienceYears

    def create(
        id_generator: UUIDGenerator,
        user: User,
        agency_name: str,
        license_number: int,
        experience_years: int
    ) -> Rieltor:
        return Rieltor(
            agency_name=RieltorAgencyName(agency_name),
            license_number=RieltorLicenseNumber(license_number),
            experience_years=RieltorExperienceYears(experience_years),
            **asdict(user)
        )
