import pytest

@pytest.fixture
def client():
    from app import app  # Import your Flask app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    # Simply test if the /test route returns status 200
    response = client.get('/test')
    
    # Assert the status code should be 200
    assert response.status_code == 200
