from dataclasses import dataclass

from app.domain.rieltor.vo_rieltor import (
    RieltorAgencyName,
    RieltorExperienceYears,
    RieltorLicenseNumber,
)
from app.domain.user.entity_user import User


@dataclass(eq=False, kw_only=True)
class Rieltor(User):
    agency_name: RieltorAgencyName
    license_number: RieltorLicenseNumber
    experience_years: RieltorExperienceYears
