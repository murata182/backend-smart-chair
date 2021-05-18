from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_chair_data,
    delete_chair_data,
    retrieve_chair_data,
    retrieve_chair_datas,
    update_chair_data,
)
from app.server.models.chair_data import (
    ErrorResponseModel,
    ResponseModel,
    ChairDataSchema,
)

router = APIRouter()

@router.post("/", response_description="Chair data added into the database")
async def add_chair_data(chair_data: ChairDataSchema = Body(...)):
#    chair_data = jsonable_encoder(chair_data)
#    new_chair_data = await add_chair_data(chair_data)
#    return ResponseModel(new_chair_data, "Chair data added successfully.")
    return chair_data

@router.get("/", response_description="Chair datas retrieved")
async def get_chair_datas():
    chair_datas = await retrieve_chair_datas()
    if chair_datas:
        return ResponseModel(chair_datas, "Chair datas retrieved successfully")
    return ResponseModel(chair_datas, "Empty list returned")


@router.get("/{id}", response_description="Chair data retrieved")
async def get_chair_data(id):
    chair_data = await retrieve_chair_data(id)
    if chair_data:
        return ResponseModel(chair_data, "Chair data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Chair data doesn't exist.")