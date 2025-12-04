import requests
from faker import Faker



class CynicalClient():
    def __init__(self):
        self.base_url = "http://94.156.115.228/"

    def registration(self, username, password):
        data = {
            "username": username,
            "email": f"{username}@mail.ru",
            "password": password
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url=f"{self.base_url}users/", json=data, headers=headers)
        return response