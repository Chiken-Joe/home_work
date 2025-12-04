import requests
from typing import Dict, Optional, Any

class CynicalApiClient():

    def __init__(self, base_url: str = "http://94.156.115.228"):
        self.base_url = base_url.rstrip('/')
        self._token: Optional[str] = None

    @property
    def headers(self) -> Dict[str, str]:
        if self._token:
            return {"Authorization": f"Bearer {self._token}"}
        return {}

    def register_user(self, username: str, email: str, password: str) -> requests.Response:
        url = f"{self.base_url}/users/"
        data = {
            "username": username,
            "email": email,
            "password": password
        }
        print(f"Отправляем запрос на регистрацию: {url}")
        print(f"Данные: {data}")

        try:
            response = requests.post(url, json=data, timeout=10)
            print(f"Статус ответа: {response.status_code}")
            if response.status_code in [200, 201]:
                print(f" Регистрация успешна!")
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при регистрации: {e}")
            class MockResponse:
                def __init__(self):
                    self.status_code = 500
                    self.text = f"Ошибка соединения: {e}"
                    self.json = lambda: {"detail": f"Ошибка соединения: {e}"}
            return MockResponse()

    def login(self, email: str, password: str) -> Optional[str]:
        url = f"{self.base_url}/auth/login/"
        data = {
            "email": email,
            "password": password
        }
        print(f"Отправляем запрос на вход: {url}")

