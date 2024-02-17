from schemas.bill import GetTipResponse, GetSourcesResponse, GetExpensesResponse
from services.bill.bill import BillService, BILL_DIR
import os

EXTRACT_DIR = "static/parser/"


class BillImpService(BillService):
    # self.ocr_model: Model

    def __init__(self):
        # self.ocr_model = Model()
        pass

    def expenses(self, bill_id: str) -> GetExpensesResponse:
        if self._should_extract(bill_id):
            self._extract_text(bill_id)

        # Generate expenses...

        return GetExpensesResponse(
            total=0,
            punta=0,
            valle=0,
            llano=0,
            max=0,
            min=0,
        )

    def sources(self, bill_id: str) -> GetSourcesResponse:
        if self._should_extract(bill_id):
            self._extract_text(bill_id)

        # Generate sources...

        return GetSourcesResponse(
            renewable=0,
            highEfficiency=0,
            naturalGas=0,
            coal=0,
            fuel=0,
            nuclear=0,
            otherNonRenewable=0,
        )

    @staticmethod
    def _should_extract(bill_id: str) -> bool:
        no_extension = bill_id.split(".")[0]
        return os.path.exists(f"{EXTRACT_DIR}/{no_extension}.txt")

    def _extract_text(self, bill_id: str):
        bill_path = f"{BILL_DIR}/{bill_id}"
        # Extract text ...
        pass

    def tip(self, bill_id: str) -> GetTipResponse:
        pass
