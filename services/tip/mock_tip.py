from schemas.bill import GetTipResponse, Tip
from services.tip.tip_service import TipService


class MockTipService(TipService):
    def tip(self, bill_id: str) -> GetTipResponse:
        return GetTipResponse(
            tips=[
                Tip(
                    tip="By looking at your usual energy consumption, you could save up to 50€ by avoiding a major "
                    "consumption Monday's at 12 PM"
                ),
                Tip(
                    tip="By how much you consume, you could save up to 30€ by avoiding a consuming as you do on "
                    "Thursday's afternoons"
                ),
                Tip(
                    tip="You could save up to 20€ by avoiding a major consumption on Sunday's at 9 PM"
                ),
                Tip(
                    tip="You could save up to 10€ by avoiding a major consumption on Saturday's at 9 PM"
                ),
                Tip(
                    tip="You could save up to 5€ by avoiding a major consumption on Friday's at 9 PM"
                ),
                Tip(
                    tip="You could save up to 5€ by avoiding a major consumption on Friday's at 9 PM"
                ),
                Tip(
                    tip="You could save up to 5€ by avoiding a major consumption on Friday's at 9 PM"
                ),
            ]
        )
