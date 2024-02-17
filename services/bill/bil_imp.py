from schemas.bill import GetTipResponse, GetSourcesResponse, GetExpensesResponse
from services.bill.bill import BillService


class BillImpService(BillService):
    def expenses(self, bill_id: str) -> GetExpensesResponse:
        pass

    def sources(self, bill_id: str) -> GetSourcesResponse:
        pass

    def tip(self, bill_id: str) -> GetTipResponse:
        pass
