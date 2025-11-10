def check_response_time(response_time):
    return response_time < 1.0
print(f"Задание 1.1: {check_response_time(0.45)}")

def check_codes_equal(code1, code2):
    return code1 == code2
print(f"Задание 1.2: {check_codes_equal(201, 201)}")

def calculate_pass_rate(total_steps, passed_steps):
    return passed_steps / total_steps
print(f"Задание 1.3: {calculate_pass_rate(10, 8)}")

def calculate_total_pages(total_items, items_per_page):
    return (total_items + items_per_page - 1) // items_per_page
print(f"Задание 1.4: {calculate_total_pages(142, 10)}")

def is_not_server_error(status_code):
    server_errors = [500, 502, 503]
    return status_code not in server_errors
print(f"Задание 1.5: {is_not_server_error(404)}")

def check_performance(response_time, status_code):
    return response_time < 0.5 and status_code == 200
print(f"Задание 1.6: {check_performance(0.2, 200)}")

def check_time_range(time_str):
    time_value = float(time_str.replace('s', ''))
    return 0.5 <= time_value <= 1.0
print(f"Задание 1.7: {check_time_range('0.82s')}")

def is_valid_response(api_response):
    return bool(api_response)
print(f"Задание 1.8: {is_valid_response('data')}")
print(f"Задание 1.8: {is_valid_response(None)}")
print(f"Задание 1.8: {is_valid_response(0)}")

def is_client_error(code):
    return 400 <= code <= 499
print(f"Задание 1.9: {is_client_error(404)}")
print(f"Задание 1.9: {is_client_error(500)}")

def check_sla(time, code):
    if 200 <= code <= 299 and time < 0.5:
        return True
    elif 400 <= code <= 499 and time < 1.0:
        return True
    return False
print(f"Задание 1.10: {check_sla(0.3, 200)}")
print(f"Задание 1.10: {check_sla(0.8, 404)}")
print(f"Задание 1.10: {check_sla(1.2, 200)}")

def build_url(base_url, endpoint):
    return f"{base_url}{endpoint}"
print(f"Задание 2.1: {build_url('https://my-api.com', '/users')}")

def clean_error_message(error_msg):
    return error_msg.strip().lower()
print(f"Задание 2.2: '{clean_error_message(' Error: Invalid Input ')}'")

def check_api_key_prefix(api_key):
    return api_key.startswith("xa-")
print(f"Задание 2.3: {check_api_key_prefix('xa-123-abc')}")

def split_log_line(log_line):
    return log_line.split(":")
print(f"Задание 2.4: {split_log_line('INFO:Test:User created')}")

def replace_price(bug_report):
    return bug_report.replace("100", "150")
print(f"Задание 2.5: {replace_price('Wrong price displayed: 100')}")

def format_user_id(user_id):
    return str(user_id).zfill(5)
print(f"Задание 2.6: {format_user_id(123)}")

def check_url_params(url_params):
    return "user=admin" in url_params and "role=qa" in url_params
print(f"Задание 2.7: {check_url_params('user=admin&role=qa')}")
print(f"Задание 2.7: {check_url_params('role=qa&user=admin')}")

def get_error_code(error_str):
    start = error_str.find("(") + 1
    end = error_str.find(")")
    return error_str[start:end]
print(f"Задание 2.8: {get_error_code('Response (404): Not Found')}")

def is_valid_uuid(uuid_str):
    return len(uuid_str) == 36 and uuid_str.count("-") == 4
print(f"Задание 2.9: {is_valid_uuid('123e4567-e89b-12d3-a456-426614174000')}")
print(f"Задание 2.9: {is_valid_uuid('invalid-uuid')}")

def parse_log(log):
    clean_log = log.strip("[]")
    parts = clean_log.split("] [", 2)
    return tuple(parts)
print(f"Задание 2.10: {parse_log('[ERROR] [auth-service] User login failed: invalid_password')}")

def create_status_codes():
    return [200, 201, 204]
print(f"Задание 3.1: {create_status_codes()}")

def add_test_result(test_results):
    test_results.append("pass")
    return test_results
print(f"Задание 3.2: {add_test_result(['pass', 'fail', 'pass'])}")

def get_max_response_time(response_times):
    return max(response_times)
print(f"Задание 3.3: {get_max_response_time([0.1, 0.5, 1.2])}")

def check_user_id(user_ids, target_id):
    return target_id in user_ids
print(f"Задание 3.4: {check_user_id([10, 20, 30, 40], 30)}")

def remove_first_smoke(tags):
    tags.remove("smoke")
    return tags
print(f"Задание 3.5: {remove_first_smoke(['smoke', 'regression', 'api', 'smoke'])}")

def sort_response_times(response_times):
    return sorted(response_times)
print(f"Задание 3.6: {sort_response_times([0.8, 0.2, 0.5])}")

def convert_to_id_strings(numbers):
    return [f"id_{num}" for num in numbers]
print(f"Задание 3.7: {convert_to_id_strings([1, 2, 3])}")

def check_same_users(expected_users, actual_users):
    return sorted(expected_users) == sorted(actual_users)
print(f"Задание 3.8: {check_same_users(['Alice', 'Bob'], ['Bob', 'Alice'])}")

def get_failed_tests(results):
    return [index for index, result in enumerate(results) if result == "fail"]
print(f"Задание 3.9: {get_failed_tests(['pass', 'fail', 'pass'])}")

def extract_user_ids(users):
    return [user["id"] for user in users]
print(f"Задание 3.10: {extract_user_ids([{'id': 1}, {'id': 2}])}")

def create_user_payload():
    return {"username": "qa_user", "role": "tester"}
print(f"Задание 4.1: {create_user_payload()}")


def get_status(response):
    return response["status"]
print(f"Задание 4.2: {get_status({'id': 123, 'status': 'ok'})}")


def add_is_active(payload):
    payload["is_active"] = True
    return payload
print(f"Задание 4.3: {add_is_active({'name': 'Test'})}")


def get_timeout(config):
    return config.get("timeout", 10)
print(f"Задание 4.4: {get_timeout({'url': 'http://api.com'})}")


def check_error_key(response):
    return "error" in response
print(f"Задание 4.5: {check_error_key({'data': {'id': 1}, 'error': None})}")


def remove_email(user_data):
    user_data.pop("email", None)
    return user_data
print(f"Задание 4.6: {remove_email({'id': 1, 'name': 'Test', 'email': 'del@me.com'})}")


def get_user_name(response):
    return response["user"]["profile"]["name"]
print(f"Задание 4.7: {get_user_name({'user': {'profile': {'name': 'Alice'}}})}")


def merge_configs(defaults, overrides):
    return {**defaults, **overrides}
print(f"Задание 4.8: {merge_configs({'timeout': 10, 'retries': 3}, {'timeout': 5, 'env': 'stage'})}")

def get_all_keys(payload):
    keys = []
    for key, value in payload.items():
        keys.append(key)
        if isinstance(value, dict):
            keys.extend(get_all_keys(value))
    return keys
print(f"Задание 4.9: {get_all_keys({'user': {'profile': {'name': 'Alice'}, 'settings': {}}})}")

def invert_dict(data):
    return {value: key for key, value in data.items()}
print(f"Задание 4.10: {invert_dict({'a': 1, 'b': 2})}")

def create_test_data():
    return ("test_login_01", "admin", "password123")
print(f"Задание 5.1: {create_test_data()}")

def unpack_test_data(test_data):
    status_code, status_text = test_data
    return f"Code: {status_code}, Text: {status_text}"
print(f"Задание 5.2: {unpack_test_data((200, 'OK'))}")

def get_unique_codes(received_error_codes):
    return set(received_error_codes)
print(f"Задание 5.3: {get_unique_codes([404, 401, 500, 404, 401])}")

def check_forbidden_code(error_codes):
    return 403 in error_codes
print(f"Задание 5.4: {check_forbidden_code({401, 404, 500})}")

def why_tuple_as_key():
    return "Кортеж неизменяем (immutable) и хешируем, а список изменяем (mutable) и не может быть ключом словаря"
print(f"Задание 5.5: {why_tuple_as_key()}")

def check_scopes(required_scopes, user_scopes):
    return required_scopes.issubset(user_scopes)
print(f"Задание 5.6: {check_scopes({'read', 'write'}, {'read', 'write', 'profile'})}")

def find_missing_tags(expected_tags, actual_tags):
    return actual_tags - expected_tags
print(f"Задание 5.7: {find_missing_tags({'api', 'v2'}, {'api', 'v1'})}")

def find_common_tags(set1, set2):
    return set1 & set2
print(f"Задание 5.8: {find_common_tags({'smoke', 'regression'}, {'regression', 'api'})}")

def has_duplicates(my_list):
    return len(my_list) != len(set(my_list))
print(f"Задание 5.9: {has_duplicates([1, 2, 3, 2])}")  # True
print(f"Задание 5.9: {has_duplicates([1, 2, 3])}")     # False

def get_unique_test_data(data):
    return set(data)
print(f"Задание 5.10: {get_unique_test_data([('user1', 'pass1'), ('user2', 'pass2'), ('user1', 'pass1')])}")

def check_status_code(status_code):
    if status_code == 200:
        return "OK"
    else:
        return "Error"
print(f"Задание 6.1: {check_status_code(401)}")


def check_user_active(is_active):
    if not is_active:
        return "User is blocked"
    return "User is active"
print(f"Задание 6.2: {check_user_active(False)}")


def check_response_body(response_body):
    if not response_body:
        return "Empty response"
    return "Response has content"
print(f"Задание 6.3: {check_response_body('')}")


def get_status_message(status_code):
    if status_code == 200:
        return "OK"
    elif status_code == 404:
        return "Not Found"
    elif status_code == 500:
        return "Server Error"
    else:
        return "Unknown status"
print(f"Задание 6.4: {get_status_message(404)}")


def evaluate_response_time(response_time):
    if response_time > 1.0:
        return "Critical: Slow"
    elif response_time > 0.5:
        return "Warning: Slowish"
    else:
        return "OK"
print(f"Задание 6.5: {evaluate_response_time(1.2)}")


def get_base_url(env):
    return "prod_url" if env == "prod" else "stage_url"
print(f"Задание 6.6: {get_base_url('prod')}")
print(f"Задание 6.6: {get_base_url('dev')}")


def check_response_data(response):
    if not response.get("data"):
        if response.get("error"):
            return f"Error: {response['error']}"
        return "No data and no error"
    return "Data is present"
print(f"Задание 6.7: {check_response_data({'data': None, 'error': 'Failed'})}")


def check_user_data(user):
    return (user.get("id", 0) > 0 and
            "@" in user.get("email", ""))
print(f"Задание 6.8: {check_user_data({'id': 1, 'email': 'test@example.com'})}")
print(f"Задание 6.8: {check_user_data({'id': 0, 'email': 'test@example.com'})}")


def check_success_response(response):
    return (response.get("status") == "success" and
            "data" in response)
print(f"Задание 6.9: {check_success_response({'status': 'success', 'data': {}})}")  # True
print(f"Задание 6.9: {check_success_response({'status': 'success'})}")  # False


def categorize_response(response):
    if not response:
        return "EMPTY"
    elif "error" in response:
        return "ERROR"
    elif "data" in response:
        return "SUCCESS"
    else:
        return "UNKNOWN"
print(f"Задание 6.10: {categorize_response(None)}")
print(f"Задание 6.10: {categorize_response({'error': 'Failed'})}")
print(f"Задание 6.10: {categorize_response({'data': {}})}")
print(f"Задание 6.10: {categorize_response({'status': 'ok'})}")

def print_browsers(browsers):
    for browser in browsers:
        print(browser)
print("Задание 7.1:")
print_browsers(["chrome", "firefox", "edge"])


def print_test_runs():
    for i in range(1, 6):
        print(f"Test run: {i}")
print("Задание 7.2:")
print_test_runs()


def print_dict_keys(payload):
    for key in payload.keys():
        print(key)
print("Задание 7.3:")
print_dict_keys({"user": "test", "pass": "123"})


def sum_response_times(response_times):
    total = 0
    for time in response_times:
        total += time
    return total
print(f"Задание 7.4: {sum_response_times([0.1, 0.5, 0.2, 1.1])}")


def check_build_status(test_statuses):
    for status in test_statuses:
        if status == "fail":
            print("Build failed!")
            break
        print(f"Status: {status}")
print("Задание 7.5:")
check_build_status(["pass", "fail", "pass"])


def print_valid_names(user_data):
    for name in user_data:
        if name is None:
            continue
        print(name)
print("Задание 7.6:")
print_valid_names(["Alice", None, "Bob"])


def print_dict_items(response):
    for key, value in response.items():
        print(f"Key: {key}, Value: {value}")
print("Задание 7.7:")
print_dict_items({"id": 1, "name": "Test"})


def print_user_names(users):
    for user in users:
        print(user["name"])
print("Задание 7.8:")
print_user_names([{"id": 1, "name": "A"}, {"id": 2, "name": "B"}])


def find_user_by_id(users_list, user_id):
    for user in users_list:
        if user["id"] == user_id:
            return user
    return None
print(f"Задание 7.9: {find_user_by_id([{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}], 2)}")


def print_matrix_elements(test_data):
    for row in test_data:
        for element in row:
            print(element)
print("Задание 7.10:")
print_matrix_elements([["user1", "pass1"], ["user2", "pass2"]])