import shutil
import os
import uuid
from PIL import Image

from fastapi import UploadFile

from services.bill.bill import BILL_DIR

IMAGE_UPLOAD_DIR = 'static/upload/'


class ImageService:
    @staticmethod
    def save_image(file: UploadFile) -> str:
        img_extension = file.filename.split(".")[-1]
        img_filename = f"{uuid.uuid4()}.{img_extension}"
        file_path = f"{IMAGE_UPLOAD_DIR}{img_filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return img_filename

    @staticmethod
    def assemble_image(image_ids: list[str]) -> str:
        images = [
            Image.open(f"{IMAGE_UPLOAD_DIR}{image_id}")
            for image_id in image_ids
        ]
        assembled_pdf_id = f"{uuid.uuid4()}.pdf"
        pdf_path = f"{BILL_DIR}{assembled_pdf_id}"
        images[0].save(
            pdf_path,
            "PDF",
            resolution=100.0,
            save_all=True,
            append_images=images[1:],
        )
        return assembled_pdf_id

    @staticmethod
    def images_exists(image_ids: list[str]) -> bool:
        return all(
            [ImageService._image_exists(image_id) for image_id in image_ids]
        )

    @staticmethod
    def _image_exists(image_id: str) -> bool:
        return os.path.exists(f"{IMAGE_UPLOAD_DIR}{image_id}")
