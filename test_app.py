import pytest
import app
from flask.testing import FlaskClient

@pytest.fixture
def client() -> FlaskClient:
    with app.app.test_client() as client:
        yield client

def test_endpoint1(client: FlaskClient):
    response = client.get('/api/endpoint1')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Hello from endpoint1'

def test_endpoint2(client: FlaskClient):
    response = client.get('/api/endpoint2')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == 'Hello from endpoint2'
