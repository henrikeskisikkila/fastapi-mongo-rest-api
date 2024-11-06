from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import dotenv_values
from routes import router

config = dotenv_values(".env")

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up")
    yield
    print("Shutting down")

app = FastAPI(lifespan=lifespan)
app.include_router(router, prefix=config["API_PREFIX"])