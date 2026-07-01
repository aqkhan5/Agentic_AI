# FastAPI Hello World & Todo REST API 🚀

A beginner-friendly project demonstrating how to build a RESTful Web API using **FastAPI** and write robust unit tests with **pytest**. 

## 🌟 Overview

This project serves as an introductory laboratory for learning FastAPI, Pydantic, and API testing. It implements a complete in-memory **Todo List CRUD API** utilizing Pydantic models for request/response serialization and validation, along with `fastapi.testclient.TestClient` for synchronous, serverless API testing.

---

## 📁 Project Structure

```
FastAPI_helloworld/
├── main.py            # FastAPI application definition and endpoints
├── test_main.py       # API test suite using pytest and TestClient
├── pyproject.toml     # Project metadata and dependencies (uv-compatible)
├── uv.lock            # uv package manager lockfile
└── README.md          # Project documentation (this file)
```

---

## 🛠️ Technical Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (>=0.136.3)
- **Data Validation**: [Pydantic v2](https://docs.pydantic.dev/) (built-in with FastAPI)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/) (>=0.49.0)
- **Testing Framework**: [pytest](https://docs.pytest.org/) (>=9.1.1)
- **Package Manager**: [uv](https://github.com/astral-sh/uv)

---

## 🔌 API Endpoints

| Method | Endpoint | Description | Request Body | Response |
|--------|----------|-------------|--------------|----------|
| **GET** | `/` | Root Hello World check | None | `{"message": "Hello World"}` |
| **GET** | `/todo` | Fetch all mock todo items | None | List of Todo items |
| **POST** | `/todo` | Create a new todo item | `TodoItem` | `TodoItemResponse` (completed=False) |
| **PUT** | `/todo/{item_id}` | Replace/Update a todo item | `TodoItem` | `TodoItemResponse` (updated) |
| **PATCH** | `/todo/{item_id}` | Partially update a todo item | `TodoItem` | `TodoItemResponse` (mocked partial update) |
| **DELETE** | `/todo/{item_id}` | Delete a todo item by ID | None | Confirmation message |

### Data Models

#### 1. `TodoItem` (Request Schema)
- `id` (int): Unique identifier
- `task` (str): Task description
- `time_estimate` (int, optional): Time estimate in minutes (defaults to `None`)

#### 2. `TodoItemResponse` (Response Schema)
- `id` (int): Unique identifier
- `task` (str): Task description
- `time_estimate` (int, optional): Time estimate in minutes
- `completed` (bool): Completion status (defaults to `False`)

---

## 🚀 Getting Started

This project is managed with the modern and extremely fast Python package manager `uv`.

### 1. Installation
Clone the repository and install dependencies using `uv`:
```bash
# Navigate to the project directory
cd FastAPI_helloworld

# Create a virtual environment and install dependencies
uv sync
```

### 2. Running the Server
Start the development server using Uvicorn:
```bash
uv run uvicorn main:app --reload
```
The API will be available at:
- **Service Endpoint**: `http://localhost:8000`
- **Interactive Documentation (Swagger UI)**: `http://localhost:8000/docs`
- **Alternative Documentation (Redoc)**: `http://localhost:8000/redoc`

### 3. Running the Test Suite
Execute the unit tests using `pytest`:
```bash
# Run pytest via uv
uv run pytest
```
Alternatively, run the test script directly:
```bash
uv run python test_main.py
```

---

## 📝 Key Learning Points

1. **Automatic Schema Generation**: FastAPI automatically generates OpenAPI documentation (`/docs`) using Pydantic models.
2. **Request Validation**: Pydantic validates incoming JSON request payloads against the `TodoItem` model, rejecting malformed requests with detailed errors.
3. **Synchronous Testing**: Using `fastapi.testclient.TestClient` allows simulating client requests directly to the ASGI application, facilitating fast and lightweight unit tests without binding to a network socket.
