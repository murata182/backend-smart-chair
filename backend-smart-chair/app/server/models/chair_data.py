from typing import Optional

from pydantic import BaseModel, Field


class ChairDataSchema(BaseModel):
    chairId: Optional[str]
    temp: Optional[int]
    presence: Optional[bool]
    noise: Optional[int]
    lum: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "chairId": "chair_01",
                "temp": 22,
                "presence": "True",
                "noise": 2,
                "lum": 3
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}