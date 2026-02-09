import pytest
from main import app
@pytest.fixture
def client():
    # Create a test client for the Flask app to simulate requests
    with app.test_client() as client:
        yield client
def test_home_json(client):
    """Test if the root endpoint returns correct JSON structure"""
    response = client.get('/')
    # 1. Check that HTTP status code is 200 OK
    assert response.status_code == 200
    # 2. Check that content-type header is 'application/json'
    assert response.is_json
    # 3. Validate the content of the JSON response
    data = response.get_json()
    assert data["service"] == "homework-api"
    assert data["status"] == "healthy"