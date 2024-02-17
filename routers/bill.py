from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi import status

from schemas.bill import (
    GetExpensesResponse,
    GetSourcesResponse,
)
from schemas.errors import NOT_FOUND, INVALID_MEDIA_TYPE
from services.bill.bil_imp import BillImpService
from services.image_service import ImageService

VALID_MEDIA_TYPES = [
    "image/jpeg",
    "image/png",
    "image/jpg",
    "application/octet-stream",
]

router = APIRouter(
    prefix="/bill",
    tags=["bill"],
)

image_service = ImageService()
bill_service = BillImpService()


@router.post(
    "/upload",
    status_code=status.HTTP_201_CREATED,
    response_model=str,
    responses={**INVALID_MEDIA_TYPE},
)
def upload_bill(
    file: UploadFile = File(...),
):
    if file.content_type not in VALID_MEDIA_TYPES:
        raise HTTPException(status_code=413, detail="Unsupported Media Type")
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
    if not image_service.images_exists(image_ids):
        raise HTTPException(status_code=404, detail="Image not found")
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
    if not bill_service.bill_exists(bill_id):
        raise HTTPException(status_code=404, detail="Bill not found")
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
    if not bill_service.bill_exists(bill_id):
        raise HTTPException(status_code=404, detail="Bill not found")
    return bill_service.sources(bill_id)
