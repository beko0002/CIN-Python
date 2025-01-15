import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"do the dishes" in response.data

def test_add_task(client):
    response = client.post("/add", data={"task": "new task"})
    assert response.status_code == 302
    response = client.get("/")
    assert b"new task" in response.data

def test_delete_task(client):
    client.post("/add", data={"task": "task to delete"})
    response = client.get("/delete/1")  # Assuming the task ID is 1
    assert response.status_code == 302
    response = client.get("/")
    assert b"task to delete" not in response.data
