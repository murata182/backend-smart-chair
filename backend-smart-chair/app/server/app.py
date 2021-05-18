from fastapi import FastAPI
from app.server.routes.chair_data import router as ChairDataRouter

app = FastAPI()

app.include_router(ChairDataRouter, tags=["ChairData"], prefix="/chair_data")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}