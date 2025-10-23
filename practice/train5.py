#Числа
#1
response_time = 0.45
print(response_time < 1.0)
#2
code1 = 201
code2 = 201
print(code1 == code2)

#3
total_steps = 10
successful_steps = 8
pass_rate = successful_steps / total_steps
print(pass_rate)
print(type(pass_rate))

#4
total_items = 142
items_per_page = 10
total_pages = (total_items + items_per_page - 1) // items_per_page  # Округление туда вот .!.
print(total_pages)
#5
import math
total_pages = math.ceil(total_items / items_per_page)
print(total_pages)

#6
status_code = 404
print(status_code not in [500, 502, 503])

#7
response_time = 0.2
status_code = 200
print(response_time < 0.5 and status_code == 200)  # True

#8
time_str = "0.82s"
time_value = float(time_str.replace('s', ''))
print(0.5 <= time_value <= 1.0)

#9
api_response = {"data": "some data"}
print(bool(api_response))

api_response = None
print(bool(api_response))

api_response = 0
print(bool(api_response))

#10
def is_client_error(code):
    return 400 <= code <= 499

print(is_client_error(404))
print(is_client_error(500))

#11
def check_sla(time, code):
    if 200 <= code <= 299 and time < 0.5:
        return True
    elif 400 <= code <= 499 and time < 1.0:
        return True
    else:
        return False
print(check_sla(0.3, 200))
print(check_sla(0.8, 404))
print(check_sla(0.6, 200))
print(check_sla(1.2, 404))

#Списки

#1
expected_status_codes = [200, 201, 204]
print(expected_status_codes)

#2
test_results = ["pass", "fail", "pass"]
test_results.append("pass")
print(test_results)

#3
response_times = [0.1, 0.5, 1.2]
max_time = max(response_times)
print(max_time)

#4
user_ids = [10, 20, 30, 40]
print(30 in user_ids)

#5
tags = ["smoke", "regression", "api", "smoke"]
tags.remove("smoke")
print(tags)

#6
response_times = [0.8, 0.2, 0.5]
response_times.sort()
print(response_times)

#7
numbers = [1, 2, 3]
string_ids = [f"id_{num}" for num in numbers]
print(string_ids)

#8
expected_users = ["Alice", "Bob"]
actual_users = ["Bob", "Alice"]
print(sorted(expected_users) == sorted(actual_users))  # True

#9
def get_failed_tests(results):
    return [index for index, result in enumerate(results) if result == "fail"]

results = ["pass", "fail", "pass", "fail"]
print(get_failed_tests(results))

#10
def get_user_ids(users):
    return [user["id"] for user in users]

users = [{"id": 1}, {"id": 2}, {"id": 3}]
print(get_user_ids(users))