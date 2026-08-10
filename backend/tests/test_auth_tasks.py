from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


TEST_EMAIL = "pytest_user@example.com"
TEST_PASSWORD = "Password123!"


def get_token():
    response = client.post(
        "/auth/login",
        json={
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD
        }
    )

    assert response.status_code == 200

    return response.json()["access_token"]


def test_register():
    response = client.post(
        "/auth/register",
        json={
            "email": TEST_EMAIL,
            "password": TEST_PASSWORD
        }
    )

    # 201 لو المستخدم جديد
    # 400 لو موجود من اختبار سابق
    assert response.status_code in [201, 400]


def test_login():
    token = get_token()

    assert token is not None
    assert len(token) > 0


def test_create_task():
    token = get_token()

    response = client.post(
        "/tasks/",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "title": "Pytest Task",
            "description": "Testing DevSecOps application"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Pytest Task"
    assert data["completed"] is False
    assert "user_id" in data


def test_get_tasks():
    token = get_token()

    response = client.get(
        "/tasks/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


def test_unauthorized_tasks():
    response = client.get("/tasks/")

    assert response.status_code in [401, 403]