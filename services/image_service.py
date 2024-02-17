import shutil
import uuid

from fastapi import UploadFile

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
