from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router

config = dotenv_values(".env")

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = MongoClient(config["MONGO_URL"])
    app.database = app.mongodb_client[config["MONGO_DB"]]
    yield
    app.mongodb_client.close()

app = FastAPI(lifespan=lifespan)
app.include_router(router, tags=["todo"], prefix=config["API_PREFIX"])