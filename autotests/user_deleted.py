import pytest
import requests


@pytest.fixture
def base_url():
    return "http://localhost:8000"



@pytest.fixture
def temp_user(base_url):
    user_data = {
        "name": "Подопотный хьюман 228",
        "email": "i.hochy.life@mail.ru",
        "password": "RaSSIAVPERED"
    }

    print(f" СОЗДАНИЕ временного хьюманса...")

    create_response = requests.post(f"{base_url}/users/", json=user_data)
    assert create_response.status_code == 201, f"Ожидался статус 201, но получили {create_response.status_code}"
    user_response_data = create_response.json()
    user_id = user_response_data.get("id")
    print(f" Хьюман создан с ID: {user_id}")
    yield user_id

    print(f" УДАЛЕНИЕ временного хьмана с ID: {user_id}...")

    delete_response = requests.delete(f"{base_url}/users/{user_id}")
    assert delete_response.status_code in [200, 204], f"Ошибка удаления: статус {delete_response.status_code}"

    print(f" Хьюман с ID: {user_id} удален")

def test_user_is_deleted_after_test(temp_user, base_url):
    user_id = temp_user

    print(f" ТЕСТ : Хьюман{user_id} будет удален после этого теста...")

    get_response = requests.get(f"{base_url}/users/{user_id}")
    assert get_response.status_code == 200

    print(f" Хьюман{user_id} существует во время теста")
