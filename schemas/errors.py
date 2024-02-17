from pydantic import BaseModel


class DetailResponseBody(BaseModel):
    detail: str


INVALID_REQUEST = {
    400: {
        "description": "Error: Invalid request",
        "model": DetailResponseBody,
    }
}

NOT_FOUND = {
    404: {
        "description": "Error: Bill not found",
        "model": DetailResponseBody,
    }
}

INVALID_MEDIA_TYPE = {
    413: {
        "description": "Error: Media type not supported",
        "model": DetailResponseBody,
    }
}
