import shutil
import pandas as pd
import uuid

from fastapi import UploadFile

from services.price_consumption.price_consumption_imp import (
    ORIGINAL_DATA_PATH,
    CSV_UPLOAD_DIR,
)


class CSVService:
    @staticmethod
    def save_csv(file: UploadFile) -> str:
        csv_extension = file.filename.split(".")[-1]
        img_filename = f"{uuid.uuid4()}.{csv_extension}"
        file_path = f"{CSV_UPLOAD_DIR}{img_filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return img_filename

    @staticmethod
    def same_headers(csv_path: str) -> bool:
        new_df = pd.read_csv(f"{CSV_UPLOAD_DIR}{csv_path}")
        new_headers = new_df.columns
        original_headers = pd.read_csv(ORIGINAL_DATA_PATH).columns
        return original_headers.equals(new_headers)
