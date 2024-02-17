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


class Tip(BaseModel):
    tip: str


class GetTipResponse(BaseModel):
    tips: list[Tip]
