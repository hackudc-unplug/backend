from fastapi import APIRouter, status, HTTPException, UploadFile, File

from schemas.errors import INVALID_REQUEST
from schemas.price_consumption import (
    GetPriceConsumptionDayResponse,
    GetPriceConsumptionWeekResponse,
    GetPriceConsumptionMonthResponse,
)
from services.date import DateService
from services.csv_service import CSVService
from services.price_consumption.price_consumption_imp import (
    PriceConsumptionImpService,
)

ACCEPTED_DATA_MIMES = ["text/csv"]

router = APIRouter(
    prefix="/price-consumption",
    tags=["price-consumption"],
)

price_consumption_service = PriceConsumptionImpService()
date_service = DateService()
csv_service = CSVService()


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


@router.post(
    "/data",
    status_code=status.HTTP_200_OK,
    responses={**INVALID_REQUEST},
)
def post_data(file: UploadFile = File(...)):
    if file.content_type not in ACCEPTED_DATA_MIMES:
        raise HTTPException(
            status_code=400, detail="Invalid file type, it must be a csv."
        )
    csv_file = csv_service.save_csv(file)
    if not CSVService.same_headers(csv_file):
        raise HTTPException(status_code=400, detail="Invalid csv headers")
    price_consumption_service.add_data(csv_file)
