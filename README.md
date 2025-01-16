# CIN-Python

This project is a simple Python Flask application containerized using Docker.
Test

## Steps to Run Locally

1. Build the Docker image:
   ```bash
   docker build -t simple-flask-app .



# Flask App Testing

## Simple Test: `/test` Route

This project includes a simple test for the `/test` route to ensure that it is functioning correctly.

### Test Description

The test checks whether the `/test` route in the Flask app returns a status code of `200`, indicating that the route is working and responding correctly.

### Test Code

```python
# import pytest

# @pytest.fixture
# def client():
#     from app import app  # Import your Flask app
#     app.config['TESTING'] = True
#     with app.test_client() as client:
#         yield client

# def test_index(client):
#     # Simply test if the /test route returns status 200
#     response = client.get('/test')
    
#     # Assert the status code should be 200
#     assert response.status_code == 200


1️⃣ Login Feature
📌 Title: User Authentication - Login

As a user,
I want to securely log in to the system using my username and password,
So that I can access my tasks and manage them.

✅ Acceptance Criteria:

User enters a valid username and password → Redirected to the dashboard.
User enters an invalid username or password → Error message is displayed.
Login form fields are required.


2️⃣ Logout Feature
📌 Title: User Logout

As a logged-in user,
I want to click a logout button,
So that I can securely end my session and prevent unauthorized access.

✅ Acceptance Criteria:

User clicks Logout → Session is cleared, and they are redirected to the login page.
Logout button is always visible on the dashboard.
If a logged-out user tries to access /, they are redirected to /login.


3️⃣ Adding a Task
📌 Title: Add a New Task

As a user,
I want to add a new task by providing a task name and optional time,
So that I can track my work efficiently.

✅ Acceptance Criteria:

User enters a task name and time selection → Task is added to the list.
Tasks are stored in an array and displayed dynamically.
The Add Task button is visible and functional.



📌 Title: Modify an Existing Task

As a user,
I want to update a task’s name or time,
So that I can correct mistakes or change the task details.

✅ Acceptance Criteria:

User clicks Update next to a task → Inputs appear for editing.
Submitting changes updates the task dynamically.
The page reloads with the updated task information.
📌 Evidence: Implemented in index.html and app.py.



📌 Title: Remove an Unwanted Task

As a user,
I want to delete a task,
So that I can remove tasks that are no longer needed.

✅ Acceptance Criteria:

Clicking Delete removes the task immediately.
The page updates dynamically, showing the task list without the deleted item.
A confirmation message appears before deletion (optional).


📌 Title: Assign a Time Duration to a Task

As a user,
I want to assign a time duration to each task using a dropdown menu,
So that I can estimate the time needed for each task.

✅ Acceptance Criteria:

Dropdown options: 15, 30, 60 minutes.
Selecting a time updates the task’s time property.
The selected time appears next to the task in the list.
