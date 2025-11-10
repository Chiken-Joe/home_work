from practice.train6 import value


def simple_calculatir(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("делить на ноль нельзя пидор!")
        return None



print(simple_calculatir(10,1))




def Error():
    response = {"status": "ok"}
    try:
        return response["data"]
    except KeyError:
        print("Дебил,ключа нет") 
        return "Ключ 'data' отсутствует"

print(f"Задание 1.2: {Error()}")

def task3():
    items = []
    try:
        return items[0]
    except IndexError:
        return "Список пуст"

print(f"Задание 1.3: {task3()}")

def task4(data_dict=None, index_list=None):
    try:
        if data_dict:
            return data_dict["missing_key"]
        if index_list:
            return index_list[10]
    except (KeyError, IndexError):
        return "Ошибка в структуре данных (отсутствует ключ или индекс)"

print(f"Задание 1.4: {task4(data_dict={'a': 1})}")

def task5():
    user_id_str = "not_a_number"
    try:
        return int(user_id_str)
    except ValueError:
        return "ID должен быть числом"

print(f"Задание 1.5: {task5()}")

def safe_get(data_dict, key):
    try:
        return [data_dict, key]
    except KeyError:
        return None

print(f"Задание 1.6: {safe_get({'Status': 'Ok'}, 'data')}")

def task7():
    response = {"status": "ok"}
    try:
        status_code = response["status_code"]
    except KeyError:
        return "Нет статус-кода"
    else:
        return f"Статус код: [status_code]"

print(f"Задание 1.7: {task7()}")

def task8():
    try:
        print("Отправка запроса...")
        raise Exception("Ошибка сети")
    finally:
        print("2. Запрос завершен (очистка)")
print(f"Задание 1.8:")

def task8(response):
    if "status" not in response:
        raise ValueError("Ответ не содержит поля 'status")
    return "Статус есть"
    


    