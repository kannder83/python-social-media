
from fastapi.testclient import TestClient
from fastapi import status
import json
from app import schemas
from typing import Dict


from app.main import app

client = TestClient(app)


def test_root():
    res = client.get("/")
    print(res.json().get("message"))
    assert res.json().get("message") == "Hello, API is working!"
    assert res.status_code == status.HTTP_200_OK


def test_create_user():
    res = client.post(
        "/users", json={"email": "hello123@gmail.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 201
