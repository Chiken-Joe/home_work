
import pytest

from clients.cynical_client import CynicalClient


# def test_first():
#     print("hello world")
#     assert 2 + 2 == 4
#
# def test_first_wrong():
#     print("nihao world")
#     assert 2 + 2 == 5



def test_success_registration():
    client = CynicalClient()
    response = client.registration("igor", "idontdomashka")
    assert response.status_code == 201, f"ты даун, ожидался 201 код, факстический:{response.status_code}, текст ответа:{response.text}"
    response.json = response.json()
    username = response.json.get("username")
    email = response.json.get("email")
    assert username == "igor" f"Неправильный парамет username,ожидался Igor, фактически  :{username}"
    assert email == f"{username}@mail.ru" f"Неправильный парамет email, ожидался {username}@mail.ru,  факстический:{email}"
