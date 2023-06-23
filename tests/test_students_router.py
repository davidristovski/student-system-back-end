import uuid

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.deps.db import get_db_session
from core.config import settings
from database.base_class import Base
from main import app

engine = create_engine(
    settings.SQLALCHEMY_TEST_DATABASE_URI, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def test_client(test_db):
    app.dependency_overrides[get_db_session] = override_get_db
    client = TestClient(app)
    yield client


def test_get_all_students_empty_db(test_client):
    response = test_client.get("/students")
    assert response.status_code == 200
    assert response.json() == []


def test_create_student(test_client):
    student_data = {
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "2000-01-01",
        "email": "john.doe@example.com",
    }
    response = test_client.post("/students", json=student_data)
    assert response.status_code == 201
    student = response.json()
    assert isinstance(student["uuid"], str)
    assert student["first_name"] == student_data["first_name"]
    assert student["last_name"] == student_data["last_name"]
    assert student["date_of_birth"] == student_data["date_of_birth"]
    assert student["email"] == student_data["email"]

    response = test_client.get(f"/students/{student['uuid']}")
    assert response.status_code == 200
    student = response.json()
    assert student["first_name"] == student_data["first_name"]
    assert student["last_name"] == student_data["last_name"]
    assert student["date_of_birth"] == student_data["date_of_birth"]
    assert student["email"] == student_data["email"]


def test_create_student_duplicate_email(test_client):
    student_data = {
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "2000-01-01",
        "email": "john.doe@example.com",
    }
    test_client.post("/students", json=student_data)
    response = test_client.post("/students", json=student_data)
    assert response.status_code == 409
    assert response.json() == {"detail": "Student already exists in the system."}


def test_delete_student(test_client):
    student_data = {
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "2000-01-01",
        "email": "john.doe@example.com",
    }
    response = test_client.post("/students", json=student_data)
    student_uuid = response.json()["uuid"]
    response = test_client.delete(f"/students/{student_uuid}")
    assert response.status_code == 204

    response = test_client.get(f"/students/{student_uuid}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student does not exist in the system."}


def test_delete_student_not_found(test_client):
    student_uuid = uuid.uuid4()

    response = test_client.delete(f"/students/{student_uuid}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Student does not exist in the system."}
