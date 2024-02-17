from schemas.bill import (
    GetExpensesResponse,
    GetSourcesResponse,
)
from services.bill.bill_service import BillService


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
