import os

from model.docparser import (
    EnergyConsumptionAnalyzer,
    EnergySourceAnalyzer,
    OCRAnalyzer,
)
from schemas.bill import GetSourcesResponse, GetExpensesResponse
from services.bill.bill_service import BillService, BILL_DIR

EXTRACT_DIR = "static/parser/"


class BillImpService(BillService):
    ocr_model: OCRAnalyzer
    output_file: str

    def __init__(self):
        self.ocr_model = OCRAnalyzer()

    def expenses(self, bill_id: str) -> GetExpensesResponse:
        self._set_output_file(bill_id)
        if self._should_extract(bill_id):
            self._extract_text(bill_id)
        consumption_analyzer = EnergyConsumptionAnalyzer(self.output_file)
        total, punta, valle, llano, maximum, minimum = (
            consumption_analyzer.parse_data()
        )

        return GetExpensesResponse(
            total=total,
            punta=punta,
            valle=valle,
            llano=llano,
            max=maximum,
            min=minimum,
        )

    def sources(self, bill_id: str) -> GetSourcesResponse:
        self._set_output_file(bill_id)
        if self._should_extract(bill_id):
            self._extract_text(bill_id)
        source_analyzer = EnergySourceAnalyzer(self.output_file)
        (
            renewable,
            highEfficiency,
            naturalGas,
            coal,
            fuel,
            nuclear,
            otherNonRenewable,
        ) = source_analyzer.parse_data()

        return GetSourcesResponse(
            renewable=renewable,
            highEfficiency=highEfficiency,
            naturalGas=naturalGas,
            coal=coal,
            fuel=fuel,
            nuclear=nuclear,
            otherNonRenewable=otherNonRenewable,
        )

    def _set_output_file(self, bill_id: str):
        no_extension = bill_id.split(".")[0]
        self.output_file = f"{EXTRACT_DIR}/{no_extension}.txt"

    @staticmethod
    def _should_extract(bill_id: str) -> bool:
        no_extension = bill_id.split(".")[0]
        return not os.path.exists(f"{EXTRACT_DIR}/{no_extension}.txt")

    def _extract_text(self, bill_id: str):
        bill_path = f"{BILL_DIR}/{bill_id}"
        no_extension = bill_id.split(".")[0]
        self.output_file = f"{EXTRACT_DIR}/{no_extension}.txt"
        self.ocr_model.parse_data_as_json(bill_path, self.output_file)
