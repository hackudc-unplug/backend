from services.image_service import IMAGE_UPLOAD_DIR
import os


def purge() -> None:
    for img in os.listdir(IMAGE_UPLOAD_DIR):
        os.remove(f"{IMAGE_UPLOAD_DIR}{img}")


if __name__ == "__main__":
    purge()
