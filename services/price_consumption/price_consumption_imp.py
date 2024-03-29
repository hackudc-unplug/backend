import datetime

import pandas as pd
import requests

from schemas.price_consumption import (
    GetPriceConsumptionMonthResponse,
    GetPriceConsumptionWeekResponse,
    GetPriceConsumptionDayResponse,
)
from services.price_consumption.price_consumption_service import (
    PriceConsumptionService,
)

ORIGINAL_DATA_PATH = "static/electrodata/electrodata.csv"
CSV_UPLOAD_DIR = 'static/data/'


class PriceConsumptionImpService(PriceConsumptionService):
    df: pd.DataFrame
    api_base_url: str

    def __init__(self):
        self.df = self._load_data()

        self.api_base_url = (
            "https://api.esios.ree.es/archives/70/download_json?date="
        )

    @staticmethod
    def _load_data() -> pd.DataFrame:
        df = pd.read_csv(ORIGINAL_DATA_PATH)
        df['datetime'] = pd.to_datetime(
            df['datetime'], format='%Y-%m-%d %H:%M:%S'
        )
        df.drop_duplicates(subset='datetime', inplace=True)
        return df

    def day_price_consumption(
        self, day: int, month: int, year: int
    ) -> GetPriceConsumptionDayResponse:
        date = datetime.datetime(year, month, day)

        consumptions = self.get_consumptions_for(date)
        prices = self.get_prices_for(date)
        return GetPriceConsumptionDayResponse(
            prices=prices, consumptions=consumptions
        )

    def week_price_consumption(
        self, day: int, month: int, year: int
    ) -> GetPriceConsumptionWeekResponse:
        consumptions: list[float] = []
        prices: list[float] = []

        date = datetime.datetime(year, month, day)
        days_since_monday = date.weekday()
        previous_monday = date - datetime.timedelta(days=days_since_monday)
        for i in range(7):
            date = previous_monday + datetime.timedelta(days=i)
            consumptions += self.get_consumptions_for(date)
            prices += self.get_prices_for(date)

        return GetPriceConsumptionWeekResponse(
            prices=prices, consumptions=consumptions
        )

    def month_price_consumption(
        self, day: int, month: int, year: int
    ) -> GetPriceConsumptionMonthResponse:
        consumptions: list[float] = []
        prices: list[float] = []

        date = datetime.datetime(year, month, day)
        date = date.replace(day=1)
        month = date.month
        while date.month == month:
            consumptions += self.get_consumptions_for(date)
            prices += self.get_prices_for(date)
            date += datetime.timedelta(days=1)

        return GetPriceConsumptionMonthResponse(
            prices=prices, consumptions=consumptions
        )

    def get_consumptions_for(self, date: datetime) -> list[float]:
        consumptions: list[float] = []
        for i in range(24):
            date = date.replace(hour=i)
            filtered_df = self.df[self.df['datetime'] == date]
            consumption = (
                filtered_df['Consumo'].iloc[0] if not filtered_df.empty else 0.0
            )
            consumptions.append(consumption)
        return consumptions

    def get_prices_for(self, date: datetime) -> list[float]:
        prices: list[float] = []
        api_date = self._date_to_api_format(date)
        api_url = self.api_base_url + api_date
        api_data = requests.get(api_url).json()

        for hour in api_data['PVPC']:
            price = hour['PCB']
            raw_price = price.replace(',', '')  # Remove incorrect comma
            euro_price = f"0.{raw_price}"  # Add 0. to turn it to euros
            prices.append(float(euro_price))
        return prices

    @staticmethod
    def _date_to_api_format(date: datetime) -> str:
        return date.strftime("%Y-%m-%d")

    def add_data(self, csv_path: str):
        new_df = pd.read_csv(f"{CSV_UPLOAD_DIR}{csv_path}")
        self.df = pd.concat([self.df, new_df])
        self.df.to_csv(ORIGINAL_DATA_PATH, index=False)
