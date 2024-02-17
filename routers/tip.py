from fastapi import APIRouter, status

from schemas.bill import GetTipResponse
from services.tip.tip_imp import TipImpService

router = APIRouter(
    prefix="/tip",
    tags=["tip"],
)

tip_service = TipImpService()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=GetTipResponse,
)
def get_tip(
    consumptions: list[float],
    prices: list[float],
):
    return tip_service.tip(consumptions, prices)
