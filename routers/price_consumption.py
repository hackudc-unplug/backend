from fastapi import APIRouter, status

from schemas.errors import INVALID_REQUEST, NOT_FOUND
from schemas.price_consumption import (
    GetPriceConsumptionDayResponse,
    GetPriceConsumptionWeekResponse,
    GetPriceConsumptionMonthResponse,
)
from services.price_consumption.mock_price_consumption import (
    MockPriceConsumptionService,
)
from services.price_consumption.price_consumption_imp import (
    PriceConsumptionImpService,
)

router = APIRouter(
    prefix="/price-consumption",
    tags=["price-consumption"],
)

# price_consumption_service = MockPriceConsumptionService()
price_consumption_service = PriceConsumptionImpService()


@router.get(
    "/day",
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
    return price_consumption_service.day_price_consumption(
        bill_id, day, month, year
    )


@router.get(
    "/week",
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
    return price_consumption_service.week_price_consumption(
        bill_id, day, month, year
    )


@router.get(
    "/month",
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
    return price_consumption_service.month_price_consumption(
        bill_id, day, month, year
    )
