import datetime
import requests
import pandas as pd

from schemas.price_consumption import (
    GetPriceConsumptionMonthResponse,
    GetPriceConsumptionWeekResponse,
    GetPriceConsumptionDayResponse,
)
from services.price_consumption.price_consumption import PriceConsumptionService


class PriceConsumptionImpService(PriceConsumptionService):
    df: pd.DataFrame
    api_base_url: str

    def __init__(self):
        self.df = pd.read_csv("static/electrodata/electrodatos.csv")
        self.df['datetime'] = pd.to_datetime(
            self.df['datetime'], format='%Y-%m-%d %H:%M:%S'
        )
        self.api_base_url = (
            "https://api.esios.ree.es/archives/70/download_json?date="
        )

    def day_price_consumption(
        self, bill_id: str, day: int, month: int, year: int
    ) -> GetPriceConsumptionDayResponse:
        date = datetime.datetime(year, month, day)

        consumptions = self.get_consumptions_for(date)
        prices = self.get_prices_for(date)
        return GetPriceConsumptionDayResponse(
            prices=prices, consumptions=consumptions
        )

    def week_price_consumption(
        self, bill_id: str, day: int, month: int, year: int
    ) -> GetPriceConsumptionWeekResponse:
        pass

    def month_price_consumption(
        self, bill_id: str, day: int, month: int, year: int
    ) -> GetPriceConsumptionMonthResponse:
        pass

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
