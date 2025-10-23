list1 = [101, 102, 103, 104, 105, 106]
list2 = [104, 105, 106, 107, 108, 109]
common_ids = set(list1).intersection(list2)
print(f"Общие ID: {common_ids}")
common_ids_list = list(set(list1) & set(list2))
print(f"Общие ID (как список): {common_ids_list}")

unique_to_list1 = set(list1).difference(list2)
print(f"Уникальные для первого списка: {unique_to_list1}")
unique_to_list1_list = list(set(list1) - set(list2))

products = [
    {"id": 1, "name": "Laptop", "price": 1000.00},
    {"id": 2, "name": "Mouse", "price": 30.13},
    {"id": 3, "name": "Keyboard", "price": 100.50}
]
all_prices_valid = all(product['price'] > 0 for product in products)

user_data = {
    "id": 123,
    "name": "Ivan Spiridonov ",
    "email": "Ivan69@email.com",
    "profile": {
        "role": "sex instructor",
        "age": 25,
        "city": "Moscow"
    },
    "is_active": True
}


name = user_data['name']
email = user_data['email']
role = user_data['profile']['role']

print(f"Имя: {name}")
print(f"Email: {email}")
print(f"Роль: {role}")


url = "/api/users/123/posts/"
user_id = url.split('/')[3]
print(f"пользовательский ID: {user_id}")


tags1 = ["python", "programming", "coding", "tech"]
tags2 = ["tech", "coding", "python", "programming"]
are_identical = set(tags1) == set(tags2)
print(f"Наборы тегов идентичны: {are_identical}")