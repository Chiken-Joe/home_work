import pytest


@pytest.fixture(scope="function")
def func_scope():
    print(" FIXTURE: func_scope СОЗДАНА (function scope)")
    return "function_data"
#Фикстура с областью видимости 'function'.Вызывается заново для КАЖДОЙ тестовой функции.

@pytest.fixture(scope="session")
def session_scope():
    print(" FIXTURE: session_scope СОЗДАНА (session scope)")
    return "session_data"
#Фикстура с областью видимости 'session'.Вызывается ОДИН РАЗ за всю сессию тестирования.

def test_one(func_scope, session_scope):
    print(f" TEST 1: func_scope='{func_scope}', session_scope='{session_scope}'")
    assert func_scope == "function_data"
    assert session_scope == "session_data"


def test_two(func_scope, session_scope):
    print(f"   TEST 2: func_scope='{func_scope}', session_scope='{session_scope}'")
    assert func_scope == "function_data"
    assert session_scope == "session_data"

def test_three(func_scope, session_scope):
    print(f"   TEST 3: func_scope='{func_scope}', session_scope='{session_scope}'")
    assert func_scope == "function_data"
    assert session_scope == "session_data"