import re
from typing import List, Tuple

from doctr.io import DocumentFile
from doctr.models import ocr_predictor


class ValueParser:
    @staticmethod
    def get_value(line: str) -> str:
        value_start = line.find("value='") + len("value='")
        value_end = line.find("'", value_start)
        return line[value_start:value_end]


class EnergyConsumption:
    def __init__(
        self, consumption_type: str, cons: float, average_price: float
    ):
        self.consumption_type = consumption_type
        self.consumption = round(cons, 3)
        self.average_price = round(average_price, 6)

    def __str__(self):
        return f"{self.consumption_type}: Energy Consumption: {self.consumption} kWh, Average Price: {self.average_price} €/kWh"


class EnergyConsumptionAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse_data(self):
        lines = self.read_lines_from_file()
        merged_data = self.merge_strings(lines)
        consumptions = self.aggregate_data(merged_data)
        min_consumption = (
            consumptions[0].consumption
            + consumptions[1].consumption
            + consumptions[2].consumption
        ) * consumptions[2].average_price
        max_consumption = (
            consumptions[0].consumption
            + consumptions[1].consumption
            + consumptions[2].consumption
        ) * consumptions[0].average_price
        punta_consumption = (
            consumptions[0].consumption * consumptions[0].average_price
        )
        llano_consumption = (
            consumptions[1].consumption * consumptions[1].average_price
        )
        valle_consumption = (
            consumptions[2].consumption * consumptions[2].average_price
        )
        total = punta_consumption + llano_consumption + valle_consumption
        return (
            round(total, 2),
            round(punta_consumption, 2),
            round(valle_consumption, 2),
            round(llano_consumption, 2),
            round(max_consumption, 2),
            round(min_consumption, 2),
        )

    def read_lines_from_file(self) -> List[str]:
        with open(self.file_path, "r") as file:
            return file.readlines()

    @staticmethod
    def merge_strings(lines: List[str]) -> List[Tuple[str, float, float]]:
        merged_strings = []
        titles = []
        merged_string = ""
        title = ""
        found_header = False
        found_title = False

        for line in lines:
            if found_title:
                if "]" in line:
                    merged_strings.append(merged_string)
                    titles.append(title)
                    merged_string = ""
                    found_title = False
                    continue
                value_start = line.find("value='") + len("value='")
                value_end = line.find("'", value_start)
                value = line[value_start:value_end]
                merged_string += value
            elif "value='Consumo'" in line:
                found_header = True
                continue
            elif found_header:
                title = ValueParser.get_value(line)
                if title in ["Punta", "Valle", "Llano"]:
                    found_title = True

        merged_strings_filtered = []
        titles_filtered = []
        print('Merged strings:', merged_strings)
        print('Titles:', titles)
        for merged_str, title in zip(merged_strings[2:], titles[2:]):
            if 'kWh' in merged_str:
                merged_strings_filtered.append(merged_str)
                titles_filtered.append(title)

        aggregated_data = {}
        for line, title in zip(merged_strings_filtered, titles_filtered):
            floats = re.findall(r'\d+,\d+', line)
            floats = [float(s.replace(',', '.')) for s in floats]
            if title not in aggregated_data:
                aggregated_data[title] = [[], []]
            aggregated_data[title][0].append(floats[0])
            aggregated_data[title][1].append(floats[1])

        parsed_data = []
        for title, values in aggregated_data.items():
            sum_first = sum(values[0])
            avg_second = sum(values[1]) / len(values[1])
            parsed_data.append((title, sum_first, avg_second))

        return parsed_data

    @staticmethod
    def aggregate_data(
        data: List[Tuple[str, float, float]]
    ) -> List[EnergyConsumption]:
        energy_consumptions = []
        for title, sum_first, avg_second in data:
            energy_consumptions.append(
                EnergyConsumption(title, sum_first, avg_second)
            )
        return energy_consumptions


class EnergySourceAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.sources = [
            "renewable",
            "highEfficiency",
            "naturalGas",
            "coal",
            "fuel",
            "nuclear",
            "otherNonRenewable",
        ]

    def parse_data(self) -> list[float]:
        lines = self.read_lines_from_file()
        source_line_index = self.find_source_line(lines)
        percentages = self.extract_percentages(lines[source_line_index:])
        return percentages

    def read_lines_from_file(self) -> List[str]:
        with open(self.file_path, "r") as file:
            return file.readlines()

    @staticmethod
    def find_source_line(lines: List[str]) -> int:
        appeared_once = False
        for i, line in enumerate(lines):
            if "S.A.U" in line:
                if appeared_once:
                    return i
                appeared_once = True

    @staticmethod
    def extract_percentages(lines: List[str]) -> List[float]:
        percentages = []
        for line in lines:
            if line.strip() == "]":
                break
            match = re.search(r"(\d+,\d+)%", line)
            if match:
                percentage = float(match.group(1).replace(',', '.'))
                percentages.append(percentage)
        return percentages


class OCRAnalyzer:
    def __init__(self):
        self.model = ocr_predictor(pretrained=True)

    def parse_data_as_json(
        self, input_file: str, output_file='out.txt'
    ) -> tuple[tuple[float, float, float, float, float, float], list[float]]:
        doc_pdf = DocumentFile.from_pdf(input_file)
        result_pdf = self.model(doc_pdf)
        with open(output_file, "w") as f:
            f.write(str(result_pdf))

        consumption_analyzer = EnergyConsumptionAnalyzer(output_file)
        source_analyzer = EnergySourceAnalyzer(output_file)

        return consumption_analyzer.parse_data(), source_analyzer.parse_data()
