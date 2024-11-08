from fastapi import APIRouter, Request, Body
from fastapi.encoders import jsonable_encoder
from models import TodoItem

router = APIRouter()

@router.post("/todos", response_description="Create a new todo", response_model=TodoItem, status_code=201)
async def create_todo(request: Request, todo: TodoItem = Body(...)):
    todo = jsonable_encoder(todo)
    new_todo = request.app.database["todos"].insert_one(todo)
    created_todo = request.app.database["todos"].find_one({"_id": new_todo.inserted_id})
    return created_todo

@router.get("/todos", response_description="List all todos", response_model=list[TodoItem])
async def list_todos(request: Request):
    todos = request.app.database["todos"].find(limit=100)
    return [todo for todo in todos]