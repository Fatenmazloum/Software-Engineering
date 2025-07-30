import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
#client is a test client (usually from FastAPI's TestClient) that lets you call your API without running the real server.
#TestClient lets you test your API without starting the server.You can send fake requests (like POST or GET) directly in your Python code.It’s like using Postman, but inside your test.
# Instead of running the FastAPI app (with uvicorn).Use a browser or a tool like Postman or curl to send a request to http://localhost:8000/some-route.