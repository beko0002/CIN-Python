def test_update_task(client):
    # Add a new task to update
    tasks.append({"task": "task to update", "added": "2025-01-14", "time": None})
    
    # Dynamically calculate the task ID
    task_id = len(tasks) - 1  # Last task index

    # Update the task
    response = client.post(f"/update/{task_id}", data={"task": "updated task"})
    assert response.status_code == 302

    # Check that the task has been updated
    response = client.get("/")
    assert b"updated task" in response.data
    assert b"task to update" not in response.data
