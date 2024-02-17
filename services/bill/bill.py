import os.path
from abc import ABC, abstractmethod

from schemas.bill import (
    GetExpensesResponse,
    GetSourcesResponse,
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
    def tip(self, bill_id: str) -> GetTipResponse:
        pass

    @staticmethod
    def bill_exists(bill_id: str) -> bool:
        return os.path.exists(f"{BILL_DIR}{bill_id}")
