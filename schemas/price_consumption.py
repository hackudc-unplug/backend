from pydantic import BaseModel


class PriceConsumptionResponse(BaseModel):
    prices: list[float]
    consumptions: list[float]


class GetPriceConsumptionDayResponse(PriceConsumptionResponse):
    pass


class GetPriceConsumptionWeekResponse(PriceConsumptionResponse):
    pass


class GetPriceConsumptionMonthResponse(PriceConsumptionResponse):
    pass
