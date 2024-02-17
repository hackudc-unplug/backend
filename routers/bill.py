from fastapi import APIRouter, UploadFile, File

from schemas.bill import (
    GetExpensesResponse,
    GetSourcesResponse,
    GetPriceConsumptionDayResponse,
    GetPriceConsumptionMonthResponse,
    GetPriceConsumptionWeekResponse,
    GetTipResponse,
)
from services.image_service import ImageService
from fastapi import status

from schemas.errors import INVALID_REQUEST, NOT_FOUND, INVALID_MEDIA_TYPE

router = APIRouter(
    prefix="/bill",
    tags=["bill"],
)

image_service = ImageService()


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
    "/{bill_id}/expenses",
    status_code=status.HTTP_200_OK,
    response_model=GetExpensesResponse,
    responses={**NOT_FOUND},
)
def get_expenses(
    bill_id: int,
):
    return {"Get": "expenses"}


@router.get(
    "/{bill_id}/sources",
    status_code=status.HTTP_200_OK,
    response_model=GetSourcesResponse,
    responses={**NOT_FOUND},
)
def get_sources(
    bill_id: int,
):
    return {"Get": "sources"}


@router.get(
    "/{bill_id}/price-consumption/day",
    status_code=status.HTTP_200_OK,
    response_model=GetPriceConsumptionDayResponse,
    responses={**NOT_FOUND, **INVALID_REQUEST},
)
def get_price_consumption_day(
    bill_id: int,
    day: str,
):
    return {"Get": "price-consumption/day"}


@router.get(
    "/{bill_id}/price-consumption/week",
    status_code=status.HTTP_200_OK,
    response_model=GetPriceConsumptionWeekResponse,
    responses={**NOT_FOUND, **INVALID_REQUEST},
)
def get_price_consumption_day(
    bill_id: int,
    week: str,
):
    return {"Get": "price-consumption/week"}


@router.get(
    "/{bill_id}/price-consumption/month",
    status_code=status.HTTP_200_OK,
    response_model=GetPriceConsumptionMonthResponse,
    responses={**NOT_FOUND, **INVALID_REQUEST},
)
def get_price_consumption_day(
    bill_id: int,
    month: str,
):
    return {"Get": "price-consumption/month"}


@router.get(
    "/{bill_id}/tip",
    status_code=status.HTTP_200_OK,
    response_model=GetTipResponse,
    responses={**NOT_FOUND},
)
def get_tip(
    bill_id: int,
):
    return {"Get": "tip"}
