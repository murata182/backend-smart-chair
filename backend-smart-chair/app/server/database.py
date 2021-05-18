import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.chair_datas

chair_data_collection = database.get_collection("chair_datas_collection")

# helpers

def chair_data_helper(chair_data) -> dict:
    return {
        "id": str(chair_data["_id"]),
        "chairId": chair_data["chairId"],
        "temp:": chair_data["temp"],
        "presence": chair_data["presence"],
        "noise": chair_data["noise"],
        "lum": chair_data["lum"]
    }



# Retrieve all chair_datas present in the database
async def retrieve_chair_datas():
    chair_datas = []
    async for chair_data in chair_data_collection.find():
        chair_datas.append(chair_data_helper(chair_data))
    return chair_datas


# Add a new chair_data into to the database
async def add_chair_data(chair_data_data: dict) -> dict:
    chair_data = await chair_data_collection.insert_one(chair_data_data)
    new_chair_data = await chair_data_collection.find_one({"_id": chair_data.inserted_id})
    return chair_data_helper(new_chair_data)


# Retrieve a chair_data with a matching ID
async def retrieve_chair_data(id: str) -> dict:
    chair_data = await chair_data_collection.find_one({"_id": ObjectId(id)})
    if chair_data:
        return chair_data_helper(chair_data)


# Update a chair_data with a matching ID
async def update_chair_data(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    chair_data = await chair_data_collection.find_one({"_id": ObjectId(id)})
    if chair_data:
        updated_chair_data = await chair_data_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_chair_data:
            return True
        return False


# Delete a chair_data from the database
async def delete_chair_data(id: str):
    chair_data = await chair_data_collection.find_one({"_id": ObjectId(id)})
    if chair_data:
        await chair_data_collection.delete_one({"_id": ObjectId(id)})
        return True