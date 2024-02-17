from fastapi import APIRouter, UploadFile, File

router = APIRouter(
    prefix="/bill",
    tags=["bill"],
)


@router.post("/upload")
def upload_bill(
    file: UploadFile = File(...),
):
    return {"Upload": "file"}


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
