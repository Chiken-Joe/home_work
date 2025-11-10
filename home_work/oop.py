def task_1():
    class TestUser:
        def __init__(self, username, email, password):
            self.username = username
            self.email = email
            self.password = password

    user = TestUser("test_user", "test@example.com", "password123")
    return f"Создан пользователь: {user.username}, {user.email}"
print(f"Задание 1: {task_1()}")


