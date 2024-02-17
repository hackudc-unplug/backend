from fastapi import APIRouter, UploadFile, File, HTTPException

from schemas.bill import (
    GetExpensesResponse,
    GetSourcesResponse,
    GetPriceConsumptionDayResponse,
    GetPriceConsumptionMonthResponse,
    GetPriceConsumptionWeekResponse,
    GetTipResponse,
)
from services.date import DateService
from services.image_service import ImageService
from fastapi import status

from schemas.errors import INVALID_REQUEST, NOT_FOUND, INVALID_MEDIA_TYPE
from services.mock_bill import MockBillService

router = APIRouter(
    prefix="/bill",
    tags=["bill"],
)

image_service = ImageService()
bill_service = MockBillService()
date_service = DateService()


@router.post(
    "/upload",
    status_code=status.HTTP_201_CREATED,
    response_model=str,
    responses={**INVALID_MEDIA_TYPE},
)
def upload_bill(
    file: UploadFile = File(...),
):
    return image_service.save_image(file)


@router.get(
    "/submit",
    status_code=status.HTTP_200_OK,
    response_model=str,
    responses={**NOT_FOUND},
)
def submit_image(
    image_id_1: str,
    image_id_2: str,
    image_id_3: str,
):
    image_ids = [image_id_1, image_id_2, image_id_3]
    # if not image_service.images_exists(image_ids):
    #     raise HTTPException(status_code=404, detail="Image not found")
    return image_service.assemble_image(image_ids)


@router.get(
    "/{bill_id}/expenses",
    status_code=status.HTTP_200_OK,
    response_model=GetExpensesResponse,
    responses={**NOT_FOUND},
)
def get_expenses(
    bill_id: str,
):
    return bill_service.expenses(bill_id)


@router.get(
    "/{bill_id}/sources",
    status_code=status.HTTP_200_OK,
    response_model=GetSourcesResponse,
    responses={**NOT_FOUND},
)
def get_sources(
    bill_id: str,
):
    # if not bill_service.bill_exists(bill_id):
    #     raise HTTPException(status_code=404, detail="Bill not found")
    return bill_service.sources(bill_id)


@router.get(
    "/{bill_id}/price-consumption/day",
    status_code=status.HTTP_200_OK,
    response_model=GetPriceConsumptionDayResponse,
    responses={**NOT_FOUND, **INVALID_REQUEST},
)
def get_price_consumption_day(
    bill_id: str,
    day: int,
    month: int,
    year: int,
):
    # if not bill_service.bill_exists(bill_id):
    #     raise HTTPException(status_code=404, detail="Bill not found")
    # if not date_service.valid_date(day, month, year):
    #     raise HTTPException(status_code=400, detail="Invalid date")
    return bill_service.day_price_consumption(bill_id, day, month, year)


@router.get(
    "/{bill_id}/price-consumption/week",
    status_code=status.HTTP_200_OK,
    response_model=GetPriceConsumptionWeekResponse,
    responses={**NOT_FOUND, **INVALID_REQUEST},
)
def get_price_consumption_day(
    bill_id: str,
    day: int,
    month: int,
    year: int,
):
    # if not bill_service.bill_exists(bill_id):
    #     raise HTTPException(status_code=404, detail="Bill not found")
    # if not date_service.valid_date(day, month, year):
    #     raise HTTPException(status_code=400, detail="Invalid date")
    return bill_service.week_price_consumption(bill_id, day, month, year)


@router.get(
    "/{bill_id}/price-consumption/month",
    status_code=status.HTTP_200_OK,
    response_model=GetPriceConsumptionMonthResponse,
    responses={**NOT_FOUND, **INVALID_REQUEST},
)
def get_price_consumption_day(
    bill_id: str,
    day: int,
    month: int,
    year: int,
):
    # if not bill_service.bill_exists(bill_id):
    #     raise HTTPException(status_code=404, detail="Bill not found")
    # if not date_service.valid_date(day, month, year):
    #     raise HTTPException(status_code=400, detail="Invalid date")
    return bill_service.month_price_consumption(bill_id, day, month, year)


@router.get(
    "/{bill_id}/tip",
    status_code=status.HTTP_200_OK,
    response_model=GetTipResponse,
    responses={**NOT_FOUND},
)
def get_tip(
    bill_id: str,
):
    # if not bill_service.bill_exists(bill_id):
    #     raise HTTPException(status_code=404, detail="Bill not found")
    return bill_service.tip(bill_id)
