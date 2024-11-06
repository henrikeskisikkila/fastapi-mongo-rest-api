from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import dotenv_values

config = dotenv_values(".env")

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up")
    yield
    print("Shutting down")

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"Hello": "World!"}