from fastapi.testclient import TestClient
from app.main import api
from app.services import users

client = TestClient(api)

user_tokens = {}
user_info = {}


def test_new_user():
    response = client.post(
        "/users/",
        json={
            "nickname": "pytest",
            "email": "pytest@pytest.com",
            "password": "12345678"
        }
    )

    assert response.status_code == 201

    assert response.json() == {
        "message": "New user created!"
    }


def test_login():
    global user_tokens

    response = client.post(
        "/users/login",
        json={
            "email": "pytest@pytest.com",
            "password": "12345678"
        }
    )

    user_tokens = response.json()

    assert response.status_code == 200


def test_me():
    global user_info

    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {user_tokens['access_token']}"}
    )

    user_info = response.json()

    assert response.status_code == 200


def test_logout():
    response = client.get(
        "/users/logout",
        headers={"Authorization": f"Bearer {user_tokens['access_token']}"}
    )

    assert response.status_code == 200


def test_delete_user():
    users.delete_user(user_info['id'])
