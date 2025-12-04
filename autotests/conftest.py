import pytest
from api_clients.cynical_client import CynicalApiClient
import time

@pytest.fixture(scope="session")
def api_client():
    return CynicalApiClient(base_url="http://localhost:8000")

@pytest.fixture(scope="session")
def api_client():
    client = CynicalApiClient(base_url="http://localhost:8000")
    print(f"\n Фикстура api_client создана (scope=session)")
    print(f"   Base URL: {client.base_url}")
    return client

def test_user_registration_login_and_me(api_client):
    timestamp = int(time.time())
    test_username = f"test_user_{timestamp}"
    test_email = f"test_{timestamp}@example.com"
    test_password = "TestPassword123!"

    print(f"\n Тестовые данные:")
    print(f"  Username: {test_username}")
    print(f"  Email: {test_email}")
    print(f"  Password: {test_password}")

    print(f"\n РЕГИСТРАЦИЯ пользователя...")
    register_response = api_client.register_user(
        username=test_username,
        email=test_email,
        password=test_password
    )

    print(f"   Статус: {register_response.status_code}")

    print(f"\n ВХОД в систему...")
    token = api_client.login(email=test_email, password=test_password)

    print(f"\n ПОЛУЧЕНИЕ информации о себе (/auth/me)...")
    me_response = api_client.get_me()
    user_data = me_response.json()
    print(f"    Данные получены!")
    print(f"   Ответ сервера: {user_data}")
