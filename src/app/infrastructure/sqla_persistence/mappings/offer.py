from sqlalchemy import UUID, Column, Enum, String, Table, Integer, Float, ForeignKey, ARRAY
from sqlalchemy.orm import composite

from app.domain.base.value_object import Id
from app.domain.offer.entity import Offer
from app.domain.offer.enums import OfferType, OfferPlaceType
from app.domain.offer.value_object import OfferArea, OfferName, OfferPrice
from app.domain.offer_details.entity import OfferDetails
from app.domain.offer_details.value_object import OfferDetailsPhoto, OfferDetailsDescription, OfferDetailsTag
from app.infrastructure.sqla_persistence.orm_registry import mapping_registry

offers_table = Table(
    "offers", 
    mapping_registry.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True),
    Column("author_id", UUID(as_uuid=True), ForeignKey("users.id"), nullable=False),
    Column(
        "place_type",
        Enum(OfferPlaceType),
        nullable=False
    ),
    Column(
        "offer_type",
        Enum(OfferType),
        nullable=False
    ),
    Column("area", Float, nullable=False),
    Column("name", String, nullable=False),
    Column("price", Integer, nullable=False),
    Column("description", String, nullable=False),
    Column("formatted_address", String, nullable=False),
    Column("photos", ARRAY(String), nullable=True),
    Column("tags", ARRAY(String), nullable=True),
)

offer_properties = {
    "id_": composite(Id, offers_table.c.id),
    "author_id": composite(Id, offers_table.c.author_id),
    "place_type": offers_table.c.place_type,
    "offer_type": offers_table.c.offer_type,
    "area": composite(OfferArea, offers_table.c.area),
    "name": composite(OfferName, offers_table.c.name),
    "price": composite(OfferPrice, offers_table.c.price),
    "formatted_address": offers_table.c.formatted_address,
}

offer_details_properties = {
    "description": composite(OfferDetailsDescription, offers_table.c.description),
    "photos": composite(list[OfferDetailsPhoto], offers_table.c.photos),
    "tags": composite(list[OfferDetailsTag], offers_table.c.tags),
    **offer_properties
}

def map_offers_table() -> None:
    mapping_registry.map_imperatively(
        Offer,
        offers_table,
        properties=offer_properties,
        column_prefix="_",
    )

def map_offer_details_table() -> None:
    mapping_registry.map_imperatively(
        OfferDetails,
        offers_table,
        properties=offer_details_properties,
        column_prefix="_",
    )
