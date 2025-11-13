import requests



class TestUser:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def to_payload(self):
        return {
             "username":self.username ,
             "email": self.email ,
             "password":self.password
             }

user = TestUser("test_user", "test@example.com", "password123")




class ApiClient:
    def __init__(self, base_url = "http://94.156.115.228/"):
        self.base_url = base_url

    def check_api_status(self):
        response = requests.get(url = self.base_url + "/")
        return response

    def create_user(self, payload):
        response = requests.post(self.base_url + "/user/", json=payload)

    def login(self, email, password):
        payload = {
        "email": email,
        "password": password
        }
        response = requests.post(self.base_url + "/auth/login/", json=payload)

        if response.status_code == 200:
            self.token = response.json().get("access_token")

        return response

    def get_me(self):
        if self.token is None:
            raise ValueError("Token is None. Зарегайся.")

        headers = {"Authorization": f"Bearer {self.token}"}
        return requests.get(self.base_url + "/auth/me/", headers=headers)


class BaseClient:
    def __init__(self, base_url="http://94.156.115.228/"):
        self.base_url = base_url
        self.session = requests.Session()

    def login(self, email, password):

        payload = {
            "email": email,
            "password": password
        }
        response = self.session.post(self.base_url + "/auth/login/", json=payload)

        if response.status_code == 200:
            token = response.json().get("access_token")
            self.session.headers['Authorization'] = f"Bearer {token}"

        return response

class UserClient(BaseClient):

    def create_user(self, payload):
        return self.session.post(self.base_url + "/users/", json=payload)

    def get_me(self):
        return self.session.get(self.base_url + "/auth/me/")












