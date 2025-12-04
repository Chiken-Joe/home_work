import pytest




def base_url():
    return "http://localhost:8000"


def test_base_url_starts_with_http(base_url):
    assert base_url.startswith("http"), f"URL {base_url} должен начинаться с 'http'"

