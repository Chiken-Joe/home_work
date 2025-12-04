import requests
import pytest




class CynicalApiClient():
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self._token = None

    @property
    def headers(self):
        if self._token:
            return {"Авторизаия": f"Bearer{self._token}"}
        return {}

    def register_user(self, username:str, email:str, password:str):
        payload = {
            "username":  username,
            "email": email,
            "password": password
        }
        return requests.post(url=f"{self.base_url}/users/", json = payload)

    def login(self, email:str, password:str ):
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(url=f"{self.base_url}/auth/login", json = payload)
        data = response.json()
        self._token = data["access_token"]
        return response

    def get_me(self):
        return requests.get(url=f"{self.base_url}/auth/me", headers = self.headers)

    def create_post(self, title: str, content: str):
        payload = {
            "title": title,
            "content": content
        }
        return requests.post(url=f"{self.base_url}/posts/", headers = self.headers, json=payload)

    def add_comment(self, post_id: str, content: str):
        payload = {
            "content": content
        }
        return requests.post(url=f"{self.base_url}/posts/{post_id}",json=payload,  headers = self.headers )

@pytest.fixture(scope="session")
def api_client():
    print("Создаем апи клиент CynicalApiClient")
    return CynicalApiClient(base_url="http://94.156.115.228")

def test_auth_flow_registe(api_client):
#РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ POST/USER/
    reg_resp = api_client.register_user(
        username = "QaMentor",
        email = "QA.mentor@itsgkola.ru",
        password = "Super_secret_password"
    )
    assert reg_resp.status_code == 201
    user_data = reg_resp.json()
    user_id = user_data["id"]


#ЛОГИНИМСЯ POST/AUTH/LOGIN

    login_resp = api_client.login(
        email = "QA.mentor@itsgkola.ru",
        password = "Super_secret_password"
    )
    assert reg_resp.status_code == 200

    # token_data = login_resp.json()
    #
    # assert "access_tolen" in token_data
    # assert token_data.get("token_type") == "bearer"

    me_resp = api_client.get_me()
    assert me_resp.status_code == 200

    me = me_resp.json()

    assert me["id"] == user_id
    assert me["email"] == "QA.mentor@itsgkola.ru"

