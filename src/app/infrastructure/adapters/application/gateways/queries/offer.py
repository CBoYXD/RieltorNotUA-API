from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.application.common.ports.gateways.queries.offer import OfferQueryGateway
from app.domain.base.value_object import Id
from app.domain.offer.entity import Offer
from app.domain.offer_details.entity import OfferDetails
from app.infrastructure.exceptions.gateways import DataMapperError

class OfferQueryGatewayImpl(OfferQueryGateway):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def read_by_id(self, offer_id: Id) -> Optional[Offer]:
        try:
            return await self._session.get_one(Offer, offer_id)
        except Exception as e:
            raise DataMapperError(f"Failed to read offer: {str(e)}")

    async def read_all(self) -> List[Offer]:
        try:
            result = await self._session.execute(select(Offer))
            return result.scalars().all()
        except Exception as e:
            raise DataMapperError(f"Failed to read all offers: {str(e)}")

    async def read_full_offer_by_id(self, offer_id: Id) -> Optional[OfferDetails]:
        try:
            return await self._session.get_one(OfferDetails, offer_id)
        except Exception as e:
            raise DataMapperError(f"Failed to read full offer: {str(e)}")

    async def read_all_full_offers(self) -> List[OfferDetails]:
        try:
            result = await self._session.execute(select(OfferDetails))
            return result.scalars().all()
        except Exception as e:
            raise DataMapperError(f"Failed to read all full offers: {str(e)}")
