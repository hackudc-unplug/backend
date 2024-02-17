import os.path
from abc import ABC, abstractmethod

from schemas.bill import (
    GetExpensesResponse,
    GetSourcesResponse,
    GetPriceConsumptionDayResponse,
    GetPriceConsumptionWeekResponse,
    GetPriceConsumptionMonthResponse,
    GetTipResponse,
)

BILL_DIR = 'static/bill/'


class BillService(ABC):
    @abstractmethod
    def expenses(self, bill_id: str) -> GetExpensesResponse:
        pass

    @abstractmethod
    def sources(self, bill_id: str) -> GetSourcesResponse:
        pass

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

    @abstractmethod
    def tip(self, bill_id: str) -> GetTipResponse:
        pass

    @staticmethod
    def bill_exists(bill_id: str) -> bool:
        return os.path.exists(f"{BILL_DIR}{bill_id}")
