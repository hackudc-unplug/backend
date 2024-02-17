from schemas.bill import GetTipResponse
from services.tip.tip_service import TipService


class TipImpService(TipService):
    def tip(self, bill_id: str) -> GetTipResponse:
        pass
