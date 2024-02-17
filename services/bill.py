from abc import ABC, abstractmethod

from schemas.bill import (
    GetExpensesResponse,
    GetSourcesResponse,
    GetPriceConsumptionDayResponse,
    GetPriceConsumptionWeekResponse,
    GetPriceConsumptionMonthResponse,
    GetTipResponse,
)


class BillService(ABC):
    @abstractmethod
    def expenses(self, bill_id: str) -> GetExpensesResponse:
        pass

    @abstractmethod
    def sources(self, bill_id: str) -> GetSourcesResponse:
        pass

    @abstractmethod
    def day_price_consumption(
        self, bill_id: str, day: str
    ) -> GetPriceConsumptionDayResponse:
        pass

    @abstractmethod
    def week_price_consumption(
        self, bill_id: str, week: str
    ) -> GetPriceConsumptionWeekResponse:
        pass

    @abstractmethod
    def month_price_consumption(
        self, bill_id: str, month: str
    ) -> GetPriceConsumptionMonthResponse:
        pass

    @abstractmethod
    def tip(self, bill_id: str) -> GetTipResponse:
        pass
