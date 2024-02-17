from fastapi import APIRouter, status, HTTPException

from schemas.errors import INVALID_REQUEST
from schemas.price_consumption import (
    GetPriceConsumptionDayResponse,
    GetPriceConsumptionWeekResponse,
    GetPriceConsumptionMonthResponse,
)
from services.date import DateService
from services.price_consumption.price_consumption_imp import (
    PriceConsumptionImpService,
)

router = APIRouter(
    prefix="/price-consumption",
    tags=["price-consumption"],
)

price_consumption_service = PriceConsumptionImpService()
date_service = DateService()


@router.get(
    "/day",
    status_code=status.HTTP_200_OK,
    response_model=GetPriceConsumptionDayResponse,
    responses={**INVALID_REQUEST},
)
def get_price_consumption_day(
    day: int,
    month: int,
    year: int,
):
    if not date_service.valid_date(day, month, year):
        raise HTTPException(status_code=400, detail="Invalid date")
    return price_consumption_service.day_price_consumption(day, month, year)


@router.get(
    "/week",
    status_code=status.HTTP_200_OK,
    response_model=GetPriceConsumptionWeekResponse,
    responses={**INVALID_REQUEST},
)
def get_price_consumption_day(
    day: int,
    month: int,
    year: int,
):
    if not date_service.valid_date(day, month, year):
        raise HTTPException(status_code=400, detail="Invalid date")
    return price_consumption_service.week_price_consumption(day, month, year)


@router.get(
    "/month",
    status_code=status.HTTP_200_OK,
    response_model=GetPriceConsumptionMonthResponse,
    responses={**INVALID_REQUEST},
)
def get_price_consumption_day(
    day: int,
    month: int,
    year: int,
):
    if not date_service.valid_date(day, month, year):
        raise HTTPException(status_code=400, detail="Invalid date")
    return price_consumption_service.month_price_consumption(day, month, year)
