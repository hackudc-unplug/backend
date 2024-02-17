from mothers.consumption import ConsumptionMother
from mothers.price import PriceMother
from schemas.bill import (
    GetExpensesResponse,
    GetSourcesResponse,
    GetTipResponse,
    Tip,
)
from services.bill.bill import BillService


class MockBillService(BillService):
    def expenses(self, bill_id: str) -> GetExpensesResponse:
        return GetExpensesResponse(
            total=124.05,
            punta=35.24,
            valle=70.49,
            llano=18.32,
            max=350.85,
            min=80.33,
        )

    def sources(self, bill_id: str) -> GetSourcesResponse:
        return GetSourcesResponse(
            renewable=33,
            highEfficiency=1.5,
            naturalGas=30.3,
            coal=3.4,
            fuel=1.3,
            nuclear=24.4,
            otherNonRenewable=6.1,
        )

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