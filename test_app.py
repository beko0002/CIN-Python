import pytest

@pytest.fixture
def client():
    from app import app  # Import your Flask app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    # Clear the session to reset any previous login state
    with client.session_transaction() as sess:
        sess.clear()

    # Now simulate logging in with valid credentials
    login_data = {
        'username': 'admin',  # Replace with a valid test username
        'password': 'password123'  # Replace with a valid test password
    }
    # POST to login route to simulate logging in
    response = client.post('/login', data=login_data)

    # Test the index route after logging in
    response = client.get('/')
    
    # Assert the status code should be 200 after login
    assert response.status_code == 200
