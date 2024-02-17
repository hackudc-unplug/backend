from pydantic import BaseModel


class GetExpensesResponse(BaseModel):
    total: float
    punta: float
    valle: float
    llano: float
    max: float
    min: float


class GetSourcesResponse(BaseModel):
    renewable: float
    highEfficiency: float
    naturalGas: float
    coal: float
    fuel: float
    nuclear: float
    otherNonRenewable: float


class Price(BaseModel):
    price: float


class Consumption(BaseModel):
    consumption: float


class PriceConsumptionResponse(BaseModel):
    prices: list[Price]
    consumptions: list[Price]


class GetPriceConsumptionDayResponse(PriceConsumptionResponse):
    pass


class GetPriceConsumptionWeekResponse(PriceConsumptionResponse):
    pass


class GetPriceConsumptionMonthResponse(PriceConsumptionResponse):
    pass


class Tip(BaseModel):
    tip: str


class GetTipResponse(BaseModel):
    tips: list[Tip]
