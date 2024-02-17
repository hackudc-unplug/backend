from docparser import EnergyConsumptionAnalyzer, EnergySourceAnalyzer, OCRAnalyzer
from schemas.bill import GetTipResponse, GetSourcesResponse, GetExpensesResponse
from services.bill.bill import BillService, BILL_DIR
import os

EXTRACT_DIR = "static/parser/"


class BillImpService(BillService):
    ocr_model: OCRAnalyzer
    output_file: str

    def __init__(self):
        self.ocr_model = OCRAnalyzer()

    def expenses(self, bill_id: str) -> GetExpensesResponse:
        if self._should_extract(bill_id):
            self._extract_text(bill_id)
        consumptionAnalyzer = EnergyConsumptionAnalyzer(self.output_file)
        total, punta, valle, llano, max, min = consumptionAnalyzer.parse_data_as_json()

        return GetExpensesResponse(
            total=total,
            punta=punta,
            valle=valle,
            llano=llano,
            max=max,
            min=min
        )

    def sources(self, bill_id: str) -> GetSourcesResponse:
        if self._should_extract(bill_id):
            self._extract_text(bill_id)
        sourceAnalyzer = EnergySourceAnalyzer(self.output_file)
        renewable, highEfficiency, naturalGas, coal, fuel, nuclear, otherNonRenewable = sourceAnalyzer.parse_data_as_json()

        return GetSourcesResponse(
            renewable=renewable,
            highEfficiency=highEfficiency,
            naturalGas=naturalGas,
            coal=coal,
            fuel=fuel,
            nuclear=nuclear,
            otherNonRenewable=otherNonRenewable
        )

    @staticmethod
    def _should_extract(bill_id: str) -> bool:
        no_extension = bill_id.split(".")[0]
        return not os.path.exists(f"{EXTRACT_DIR}/{no_extension}.txt")

    def _extract_text(self, bill_id: str):
        bill_path = f"{BILL_DIR}/{bill_id}"
        no_extension = bill_id.split(".")[0]
        self.output_file = f"{EXTRACT_DIR}/{no_extension}.txt"
        self.ocr_model.parse_data_as_json(bill_path, self.output_file)

    def tip(self, bill_id: str) -> GetTipResponse:
        pass
