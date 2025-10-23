def pagination_analyzer(total_items , items_per_page):
    full_pages = total_items // items_per_page
    remaining_items = total_items % items_per_page
    return f"всего полных страниц: {full_pages}. Товаров на последней странице: {remaining_items}"
total_items = 127
items_per_page = 10
result = pagination_analyzer(total_items, items_per_page)
print(result)


def validate_active_status(value):
    if isinstance(value, str):
        value = value.lower().strip()
    if value in [True, 1, "true", "1", "yes"]:
        return True
    return False
test_values = [1, "", "true", None]
results = [validate_active_status(val) for val in test_values]
print("Результаты:")
for i, (input_val, output_val) in enumerate(zip(test_values, results)):
    print(f"  {input_val!r} -> {output_val}")
print(f"\nитоговый результат: {results}")


def extract_user_id(url):
    parts = url.split('/')
    if 'users' in parts:
        users_index = parts.index('users')
        if users_index + 1 < len(parts):
            user_id = parts[users_index + 1]
            if user_id.isdigit():
                return int(user_id)
            return None
        print(f"\nвходные данные: '/api/v2/users/1337/profile/'")
print(f"ожидаемый результат: {extract_user_id('/api/v2/users/1337/profile/')}")



def normalize_name(name):
    cleaned_name = ' '.join(name.strip().split())
    normalized_name = cleaned_name.title()
    return normalized_name
print(f"\nВходные данные: ' jane smith '")
print(f"Ожидаемый результат: '{normalize_name(' jane smith ')}'")




def filter_available_products( products ):
    return [product for product in products if product.get('quantity', 0) > 0]
products = [
    {"name": "Book", "quantity": 10},
    {"name": "Pen", "quantity": 0},
    {"name": "Laptop", "quantity": 5}
]
result = filter_available_products(products)
print("Отфильтрованные товары:")
for product in result:
    print(f"  {product['name']}: {product['quantity']} шт.")
print(f"\nОжидаемый результат: {result}")



def check_permissions( user_permissions , required_permissions ):
    user_set = set( user_permissions )
    required_set = set(required_permissions)
    return required_set.issubset(user_set)
user_permissions = ["read", "comment", "write"]
required_permissions = ["write", "read"]
result = check_permissions(user_permissions, required_permissions)
print(f"Права пользователя: {user_permissions}")
print(f"Обязательные права: {required_permissions}")
print(f"Доступ разрешен: {result}")
print(f"\nОжидаемый результат: {result}")


def get_user_city(user):
    if isinstance(user.get('address'), dict):
        city = user['address'].get('city')
        if city is not None:
            return city
    return "Город не указан"
user1 = {"id": 1, "name": "Alex", "address": {"city": "Berlin", "street": "Main str."}}
user2 = {"id": 2, "name": "Bob"}
result1 = get_user_city(user1)
result2 = get_user_city(user2)
print(f"Пользователь 1: {result1}")
print(f"Пользователь 2: {result2}")
print(f"\nОжидаемый результат: '{result1}' и '{result2}'")



def create_patch_update(current_data, updates):
    patch_data = {}
    for key, new_value in updates.items():
        if key not in current_data or current_data[key] != new_value:
            patch_data[key] = new_value
    return patch_data
current = {"name": "Olga", "age": 30, "role": "user"}
updates = {"age": 31, "role": "user"}
result = create_patch_update(current, updates)
print(f"Исходные данные: {current}")
print(f"Обновления: {updates}")
print(f"PATCH-запрос: {result}")
print(f"\nОжидаемый результат: {result}")



def compare_tags(api_tags, expected_tags):
    api_set = set(api_tags)
    expected_set = set(expected_tags)
    return api_set == expected_set
api_tags = ["python", "qa", "testing", "python"]
expected_tags = ["qa", "python", "testing"]
result = compare_tags(api_tags, expected_tags)
print(f"Теги из API: {api_tags}")
print(f"Ожидаемые теги: {expected_tags}")
print(f"Результат сравнения: {result}")
print(f"\nОжидаемый результат: {result}")



def find_unprocessed_ids(expected_ids, processed_ids):
    expected_set = set(expected_ids)
    processed_set = set(processed_ids)
    return expected_set - processed_set
expected_ids = [10, 20, 30, 40, 50]
processed_ids = [20, 50, 10]
result = find_unprocessed_ids(expected_ids, processed_ids)
print(f"Ожидаемые ID: {expected_ids}")
print(f"Обработанные ID: {processed_ids}")
print(f"Необработанные ID: {result}")
print(f"\nОжидаемый результат: {result}")