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
    def __init__(self, base_url):
        self.base_url = base_url

    def check_api_status(self):
        response = requests.get(url = self.base_url + "/")
        return response

    def create_user(self, payload):
        response = requests.post(self.base_url + "/user/", json=payload)
















