import pytest

from practice.train3 import email
from practice.train6 import response, username


@pytest.mark.smoke
def test_create_user_smoke(api_client):
    response = api_client.register_user(
        username="smokee_user",
        email="smokee@mail.ru",
        password="smokee"
    )
    assert response.status_code == 201