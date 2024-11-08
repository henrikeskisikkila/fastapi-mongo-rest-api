from fastapi.testclient import TestClient
from dotenv import dotenv_values
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.testclient import TestClient
from routes import router
from pymongo import MongoClient
from main import app

client = TestClient(app)
config = dotenv_values(".env")
app.include_router(router, tags=["todo"], prefix=config["API_PREFIX"])

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = MongoClient(config["MONGO_URL"])
    app.database = app.mongodb_client[config["MONGO_DB"]]
    yield
    app.mongodb_client.close()
    app.database.drop_collection("todos")
    app.mongodb_client.close()

def test_create_todo():
    with TestClient(app) as client:
        response = client.post("/api/v1/todos", json={"title": "Test Todo", "description": "This is a test todo"})
        assert response.status_code == 201
        body = response.json()
        assert body.get("title") == "Test Todo"
        assert body.get("description") == "This is a test todo"

def test_list_todos():
    with TestClient(app) as client:
        response = client.get("/api/v1/todos")
        assert response.status_code == 200
        body = response.json()
        assert len(body) >= 1

def test_get_todo():
    with TestClient(app) as client:
        response = client.post("/api/v1/todos", json={"title": "Test Todo", "description": "This is a test todo"})
        assert response.status_code == 201
        body = response.json()
        todo_id = body["_id"]

        response = client.get(f"/api/v1/todos/{todo_id}")
        assert response.status_code == 200
        body = response.json()
        assert body.get("title") == "Test Todo"
        assert body.get("description") == "This is a test todo"

def test_update_todo():
    with TestClient(app) as client:
        response = client.post("/api/v1/todos", json={"title": "Test Todo", "description": "This is a test todo"})
        assert response.status_code == 201
        body = response.json()
        todo_id = body["_id"]

        # Update the created todo
        updated_todo = {
            "title": "Test Todo",
            "description": "This is a test todo",
            "completed": True
        }
        response = client.put(f"/api/v1/todos/{todo_id}", json=updated_todo)
        assert response.status_code == 200
        body = response.json()
        assert body.get("completed") == True

def test_delete_todo():
    with TestClient(app) as client:
        response = client.post("/api/v1/todos", json={"title": "Test Todo", "description": "This is a test todo"})
        assert response.status_code == 201
        body = response.json()
        todo_id = body["_id"]

        response = client.delete(f"/api/v1/todos/{todo_id}")
        assert response.status_code == 200
        body = response.json()
        assert body.get("message") == "Todo deleted successfully"
