# REST API with FastAPI and MongoDB

This is a REST API template project built using FastAPI and MongoDB. You can use this project as an example to get started with a FastAPI backend that uses MongoDB. If you find this project useful, please drop a star.

## Features

- FastAPI for building the REST API
- MongoDB for data storage
- Pydantic for data validation
- dotenv for environment variable management

## Requirements

- Python 3.7+
- MongoDB

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/henrikeskisikkila/mongo-fastapi.git
   cd mongo-fastapi
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your MongoDB connection string:
   ```properties
   MONGO_URL=your_mongodb_connection_string
   MONGO_DB=your_database_name
   API_PREFIX=/api/v1
   ```

## Running the Server

Start the server with the following command:
```bash
uvicorn main:app --reload
```

The server will be running at `http://127.0.0.1:8000`.

## Running tests

Run tests:
```bash
pytest
```


## API Endpoints

### Create a new todo
- **URL**: `/api/v1/todos`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "title": "Sample Todo",
    "description": "This is a sample todo item",
    "completed": false
  }
  ```
- **Response**:
  ```json
  {
    "_id": "generated_id",
    "title": "Sample Todo",
    "description": "This is a sample todo item",
    "completed": false
  }
  ```

### List all todos
- **URL**: `/api/v1/todos`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {
      "_id": "generated_id",
      "title": "Sample Todo",
      "description": "This is a sample todo item",
      "completed": false
    },
    ...
  ]
  ```

### Get a specific todo
- **URL**: `/api/v1/todos/{todo_id}`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "_id": "generated_id",
    "title": "Sample Todo",
    "description": "This is a sample todo item",
    "completed": false
  }
  ```

### Update a specific todo
- **URL**: `/api/v1/todos/{todo_id}`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "title": "Updated Todo",
    "description": "This is an updated todo item",
    "completed": true
  }
  ```
- **Response**:
  ```json
  {
    "_id": "generated_id",
    "title": "Updated Todo",
    "description": "This is an updated todo item",
    "completed": true
  }
  ```

### Delete a specific todo
- **URL**: `/api/v1/todos/{todo_id}`
- **Method**: `DELETE`
- **Response**: `204 No Content`

## License

This project is licensed under the MIT License.