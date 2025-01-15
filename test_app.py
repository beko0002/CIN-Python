import pytest
from app import app
from app import tasks  # Import the global tasks list

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
    # Add a new task directly to the tasks list
    tasks.append({"task": "task to delete", "added": "2025-01-14"})
    
    # Dynamically calculate the task ID
    task_id = len(tasks) - 1  # Last task index
    
    # Delete the task
    response = client.get(f"/delete/{task_id}")
    assert response.status_code == 302
    
    # Check that the task is no longer in the list
    response = client.get("/")
    assert b"task to delete" not in response.data

