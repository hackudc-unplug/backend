from fastapi import APIRouter, status

from schemas.bill import GetTipResponse
from schemas.errors import NOT_FOUND

router = APIRouter(
    prefix="/tip",
    tags=["tip"],
)


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
