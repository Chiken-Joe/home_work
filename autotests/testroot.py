import requests
import json


def test_get_root():
    response = requests.get("https://api.cynicalcircle.com/")
    assert response.status_code == 200, f"Ожидался статус 200, но получили {response.status_code}"
