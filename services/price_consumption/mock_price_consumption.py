from mothers.consumption import ConsumptionMother
from mothers.price import PriceMother
from schemas.price_consumption import (
    GetPriceConsumptionDayResponse,
    GetPriceConsumptionWeekResponse,
    GetPriceConsumptionMonthResponse,
)
from services.price_consumption.price_consumption_service import (
    PriceConsumptionService,
)


class MockPriceConsumptionService(PriceConsumptionService):
    def day_price_consumption(
        self, day: int, month: int, year: int
    ) -> GetPriceConsumptionDayResponse:
        return GetPriceConsumptionDayResponse(
            prices=PriceMother.get_daily_prices(),
            consumptions=ConsumptionMother.get_daily_consumptions(),
        )

    def week_price_consumption(
        self, day: int, month: int, year: int
    ) -> GetPriceConsumptionWeekResponse:
        return GetPriceConsumptionWeekResponse(
            prices=PriceMother.get_weekly_prices(),
            consumptions=ConsumptionMother.get_weekly_consumptions(),
        )

    def month_price_consumption(
        self, day: int, month: int, year: int
    ) -> GetPriceConsumptionMonthResponse:
        return GetPriceConsumptionMonthResponse(
            prices=PriceMother.get_monthly_prices(),
            consumptions=ConsumptionMother.get_monthly_consumptions(),
        )
