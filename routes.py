from fastapi import APIRouter

router = APIRouter()

@router.get("/ping", response_description="Ping pong", status_code=200)
async def ping():
    return {"ping": "pong"}