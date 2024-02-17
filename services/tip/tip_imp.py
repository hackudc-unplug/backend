from model.tip_llm import TipLLM
from schemas.bill import GetTipResponse
from services.tip.tip_service import TipService


class TipImpService(TipService):
    tip_model: TipLLM

    def __init__(self):
        self.tip_model = TipLLM()

    def tip(
        self, consumptions: list[float], prices: list[float]
    ) -> GetTipResponse:
        tips = self.tip_model.get_tip_for_day(consumptions, prices)
        return GetTipResponse(tip=tips)
