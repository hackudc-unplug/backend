from schemas.bill import GetTipResponse
from services.tip.tip_service import TipService


class MockTipService(TipService):
    def tip(
        self, consumptions: list[float], prices: list[float]
    ) -> GetTipResponse:
        return GetTipResponse(
            tip="""
            1. Move high consumption from the most expensive hours (17, 0, 14) to cheaper hours like [23, 16, 
            22]. For example, consider moving your evening TV show from 7 pm to 11 pm, when electricity rates are lower.

            2. Identify the most consumed hours (4, 23, 12) and see if there's anything you can do to reduce usage during those 
            times. For instance, consider rescheduling your daily morning coffee session to a later time when you're not rushing 
            to get to work or school.

            3. Focus on reducing consumption during the least expensive hours ([19, 7, 0]). Consider using energy-efficient 
            appliances and turning off appliances that are not in use, such as lights and televisions, when you leave a room.

            By following these tips, you can not only lower your electricity costs but also help conserve energy and reduce your 
            carbon footprint.
            """
        )
