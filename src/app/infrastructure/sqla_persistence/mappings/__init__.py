"""
Ensures imperative SQLAlchemy mappings are initialized at application startup.

### Purpose:
In Clean Architecture, domain entities remain agnostic of database
mappings. To integrate with SQLAlchemy, mappings must be explicitly
triggered to link ORM attributes to domain classes. Without this setup,
attempts to interact with unmapped entities in database operations
will lead to runtime errors.

### Solution:
This file provides a single entry point to initialize the mapping
of domain entities to database tables. By calling the `map_tables` function,
ORM attributes are linked to domain classes without altering domain code
or introducing infrastructure concerns.

### Usage:
Call the `map_tables` function in the application factory to initialize
mappings at startup. Additionally, it is necessary to call this function
in `env.py` for Alembic migrations to ensure all models are available
during database migrations.
"""

from app.infrastructure.sqla_persistence.mappings.user import map_users_table
from app.infrastructure.sqla_persistence.mappings.offer import map_offers_table, map_offer_details_table
from app.infrastructure.sqla_persistence.mappings.rieltor import map_rieltors_table


def map_tables() -> None:
    map_users_table()
    map_offers_table()
    map_offer_details_table()
    map_rieltors_table()

