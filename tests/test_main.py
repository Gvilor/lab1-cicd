import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, from docker test1"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_calculate_sum():
    response = client.post("/sum", json={"a": 5, "b": 7})
    assert response.status_code == 200
    assert response.json() == {"result": 12}


def test_multiply():
    response = client.get("/multiply?a=3&b=4")
    assert response.status_code == 200
    assert response.json() == {"result": 12}