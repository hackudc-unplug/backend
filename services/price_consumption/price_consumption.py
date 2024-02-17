from abc import ABC, abstractmethod

from schemas.price_consumption import (
    GetPriceConsumptionDayResponse,
    GetPriceConsumptionWeekResponse,
    GetPriceConsumptionMonthResponse,
)


class PriceConsumptionService(ABC):
    @abstractmethod
    def day_price_consumption(
        self,
        bill_id: str,
        day: int,
        month: int,
        year: int,
    ) -> GetPriceConsumptionDayResponse:
        pass

    @abstractmethod
    def week_price_consumption(
        self,
        bill_id: str,
        day: int,
        month: int,
        year: int,
    ) -> GetPriceConsumptionWeekResponse:
        pass

    @abstractmethod
    def month_price_consumption(
        self,
        bill_id: str,
        day: int,
        month: int,
        year: int,
    ) -> GetPriceConsumptionMonthResponse:
        pass
