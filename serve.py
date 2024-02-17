import uvicorn
import os

from services.bill.bil_imp import EXTRACT_DIR
from services.image_service import IMAGE_UPLOAD_DIR
from services.bill.bill_service import BILL_DIR

if __name__ == "__main__":
    if not os.path.exists(EXTRACT_DIR):
        os.makedirs(EXTRACT_DIR)
    if not os.path.exists(IMAGE_UPLOAD_DIR):
        os.makedirs(IMAGE_UPLOAD_DIR)
    if not os.path.exists(BILL_DIR):
        os.makedirs(BILL_DIR)
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
