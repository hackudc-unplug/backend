from fastapi import APIRouter, UploadFile, File
from services.image_service import ImageService
from fastapi import status

from schemas.errors import INVALID_REQUEST

router = APIRouter(
    prefix="/bill",
    tags=["bill"],
)

image_service = ImageService()


@router.post(
    "/upload",
    status_code=status.HTTP_201_CREATED,
    response_model=str,
    responses={**INVALID_REQUEST},
)
def upload_bill(
    file: UploadFile = File(...),
):
    return image_service.save_image(file)


@router.get("/{bill_id}/expenses")
def get_expenses(
    bill_id: int,
):
    return {"Get": "expenses"}


@router.get("/{bill_id}/sources")
def get_sources(
    bill_id: int,
):
    return {"Get": "sources"}


@router.get("/{bill_id}/price-consumption/day")
def get_price_consumption_day(
    bill_id: int,
    day: str,
):
    return {"Get": "price-consumption/day"}


@router.get("/{bill_id}/price-consumption/month")
def get_price_consumption_day(
    bill_id: int,
    month: str,
):
    return {"Get": "price-consumption/month"}


@router.get("/{bill_id}/price-consumption/week")
def get_price_consumption_day(
    bill_id: int,
    week: str,
):
    return {"Get": "price-consumption/week"}


@router.get("/{bill_id}/tip")
def get_tip(
    bill_id: int,
):
    return {"Get": "tip"}
