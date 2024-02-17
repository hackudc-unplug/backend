from abc import ABC, abstractmethod

from schemas.bill import GetTipResponse


class TipService(ABC):
    @abstractmethod
    def tip(
        self, consumptions: list[float], prices: list[float]
    ) -> GetTipResponse:
        pass
