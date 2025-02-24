from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete

from app.application.common.ports.gateways.command.offer import OfferCommandGateway
from app.domain.base.value_object import Id
from app.domain.offer.entity import Offer
from app.domain.offer_details.entity import OfferDetails
from app.infrastructure.exceptions.gateways import DataMapperError

class OfferCommandGatewayImpl(OfferCommandGateway):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, offer: Offer) -> None:
        """
        Save an offer to the database.
        
        :param offer: The offer entity to save
        :raises DataMapperError: If database operation fails
        """
        try:
            self._session.add(offer)
        except Exception as e:
            raise DataMapperError(f"Failed to save offer: {str(e)}")

    async def save_details(self, offer_details: OfferDetails) -> None:
        """
        Save offer details to the database.
        
        :param offer_details: The offer details entity to save
        :raises DataMapperError: If database operation fails
        """
        try:
            self._session.add(offer_details)
        except Exception as e:
            raise DataMapperError(f"Failed to save offer details: {str(e)}")

    async def delete(self, offer_id: Id) -> None:
        """
        Delete an offer by its ID.
        
        :param offer_id: ID of the offer to delete
        :raises DataMapperError: If database operation fails
        """
        try:
            await self._session.delete(offer)
        except Exception as e:
            raise DataMapperError(f"Failed to delete offer: {str(e)}")

    async def delete_all(self, user_id: Id) -> None:
        """
        Delete all offers for a specific user.
        
        :param user_id: ID of the user whose offers should be deleted
        :raises DataMapperError: If database operation fails
        """
        try:
            await self._session.execute(delete(Offer))
        except Exception as e:
            raise DataMapperError(f"Failed to delete all offers: {str(e)}")
