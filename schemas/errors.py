from pydantic import BaseModel


class DetailResponseBody(BaseModel):
    detail: str


INVALID_REQUEST = {
    400: {
        "description": "Error: Invalid file type",
        "model": DetailResponseBody,
    }
}
