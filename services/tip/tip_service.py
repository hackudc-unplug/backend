from abc import ABC, abstractmethod

from schemas.bill import GetTipResponse


class TipService(ABC):
    @abstractmethod
    def tip(self, bill_id: str) -> GetTipResponse:
        pass
