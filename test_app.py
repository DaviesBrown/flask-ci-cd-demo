from app import app


def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from Flask" in response.data


def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200


def test_info():
    client = app.test_client()
    response = client.get('/api/info')
    assert response.status_code == 200
    
    data = response.get_json()
    assert "app_name" in data
    assert "version" in data
    assert "timestamp" in data
    assert "endpoints" in data
    assert data["app_name"] == "Flask CI/CD Demo"
    assert data["version"] == "1.0.0"
    assert isinstance(data["endpoints"], list)
    assert len(data["endpoints"]) == 3
