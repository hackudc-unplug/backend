from typing import List, Tuple
import re
import json
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

class ValueParser:
    @staticmethod
    def get_value(line: str) -> str:
        value_start = line.find("value='") + len("value='")
        value_end = line.find("'", value_start)
        return line[value_start:value_end]

class EnergyConsumption:
    def __init__(self, consumption_type: str, consumption: float, average_price: float):
        self.consumption_type = consumption_type
        self.consumption = round(consumption, 3)
        self.average_price = round(average_price, 6) 

    def __str__(self):
        return f"{self.consumption_type}: Energy Consumption: {self.consumption} kWh, Average Price: {self.average_price} €/kWh"

class EnergyConsumptionAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse_data_as_json(self) -> List[EnergyConsumption]:
        lines = self.read_lines_from_file()
        merged_data = self.merge_strings(lines)
        consumptions = self.aggregate_data(merged_data)
        min_consumption = (consumptions[0].consumption + consumptions[1].consumption + consumptions[2].consumption) * consumptions[2].average_price
        max_consumption = (consumptions[0].consumption + consumptions[1].consumption + consumptions[2].consumption) * consumptions[0].average_price
        punta_consumption = consumptions[0].consumption * consumptions[0].average_price
        llano_consumption = consumptions[1].consumption * consumptions[1].average_price
        valle_consumption = consumptions[2].consumption * consumptions[2].average_price
        total = punta_consumption + llano_consumption + valle_consumption

        data = {
            "total": round(total, 2),
            "punta": round(punta_consumption, 2),
            "valle": round(valle_consumption, 2),
            "llano": round(llano_consumption, 2),
            "max": round(max_consumption, 2),
            "min": round(min_consumption, 2)
        }

        return json.dumps(data, indent=2)
        

    def read_lines_from_file(self) -> List[str]:
        with open(self.file_path, "r") as file:
            return file.readlines()

    def merge_strings(self, lines: List[str]) -> List[Tuple[str, float, float]]:
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
        for merged_str, title in zip(merged_strings[2:], titles[2:]):
            if merged_str.lstrip()[0].isdigit():
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

    def aggregate_data(self, data: List[Tuple[str, float, float]]) -> List[EnergyConsumption]:
        energy_consumptions = []
        for title, sum_first, avg_second in data:
            energy_consumptions.append(EnergyConsumption(title, sum_first, avg_second))
        return energy_consumptions
    

class EnergySourceAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.sources = ["renewable", "highEfficiency", "naturalGas", "coal", "fuel", "nuclear", "otherNonRenewable"]

    def parse_data_as_json(self) -> str:
        lines = self.read_lines_from_file()
        source_line_index = self.find_source_line(lines)
        percentages = self.extract_percentages(lines[source_line_index:])
        data = {source: percentage for source, percentage in zip(self.sources, percentages)}
        return json.dumps(data, indent=2)

    def read_lines_from_file(self) -> List[str]:
        with open(self.file_path, "r") as file:
            return file.readlines()

    def find_source_line(self, lines: List[str]) -> int:
        appeared_once = False
        for i, line in enumerate(lines):
            if "S.A.U" in line:
                if appeared_once:
                    return i
                appeared_once = True

    def extract_percentages(self, lines: List[str]) -> List[float]:
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

    def parse_data_as_json(self, input_file: str, output_file='out.txt') -> Tuple[str, str]:
        doc_pdf = DocumentFile.from_pdf(input_file)
        result_pdf = self.model(doc_pdf)
        with open(output_file, "w") as f:
            f.write(str(result_pdf))

        consumptionAnalyzer = EnergyConsumptionAnalyzer(output_file)
        sourceAnalyzer = EnergySourceAnalyzer(output_file)

        return (consumptionAnalyzer.parse_data_as_json(), sourceAnalyzer.parse_data_as_json())
        

if __name__ == "__main__":
    ocr_analyzer = OCRAnalyzer()
    consumption, sources = ocr_analyzer.parse_data_as_json("factura-sencera-pdf.pdf")
    print(consumption)
    print(sources)
