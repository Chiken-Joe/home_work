#Строки
#1
base_url = "https://my-api.com"
endpoint = "/users"
full_url = f"{base_url}{endpoint}"
print(full_url)
#2
error_msg = " Error: Invalid Input "
clean_msg = error_msg.strip().lower()
#3
api_key = "xa-123-abc"
result = api_key.startswith("xa-")
#4
log_line = "INFO:Test:User created"
parts = log_line.split(":")
#5
bug_report = "Wrong price displayed: 100"
updated_report = bug_report.replace("100", "150")
#6
user_id = 123
formatted_id = str(user_id).zfill(5)
#7
url_params = "user=admin&role=qa"
has_user = "user=admin" in url_params
has_role = "role=qa" in url_params
result = has_user and has_role
#8
def get_error_code_split(error_str):
    try:
        return error_str.split('(')[1].split(')')[0]
    except IndexError:
        return None
#9
def is_valid_uuid(uuid_str):
    return len(uuid_str) == 36 and uuid_str.count('-') == 4
#10
def parse_log(log):
    log = log.strip('[]')
    parts = log.split(']', 1)
    if len(parts) == 2:
        level = parts[0].strip()
        remaining = parts[1].strip()
        service_msg = remaining.split(':', 1)
        if len(service_msg) == 2:
            service = service_msg[0].strip().strip('[]')
            message = service_msg[1].strip()
            return (level, service, message)

    return (None, None, None)



#словари
#1
api_payload = {"username": "qa_user", "role": "tester"}
#2
status = response.get("status")
#3
payload.update({"is_active": True})
#4
config = {"url": "http://api.com"}
timeout = config.get("timeout", 10)
#5
response = {"data": {"id": 1}, "error": None}
has_error = "error" in response
#6
user_data = {"id": 1, "name": "Test", "email": "del@me.com"}
del user_data["email"]
#7
name = response.get("user", {}).get("profile", {}).get("name")
#8
defaults = {"timeout": 10, "retries": 3}
overrides = {"timeout": 5, "env": "stage"}
#9
def get_all_keys(payload, parent_key=''):
    keys = []
    for key, value in payload.items():
        full_key = f"{parent_key}.{key}" if parent_key else key
        keys.append(full_key)
        if isinstance(value, dict):
            keys.extend(get_all_keys(value, full_key))
    return keys
#10
def invert_dict(data):
    #????


#Кортежи
#1
test_data = ("test_login_01", "admin", "password123")
#2
test_data = (200, "OK")
status_code, status_text = test_data
#3
received_error_codes = [404, 401, 500, 404, 401]
unique_codes = set(received_error_codes)
#4
error_codes = {401, 404, 500}
has_403 = 403 in error_codes
#5
#кортежи неизменяемы (immutable), поэтому их хеш-значение не меняется,
#что позволяет использовать их как ключи словаря. Списки изменяемы (mutable),
#их хеш-значение может измениться, поэтому они не могут быть ключами словаря
#valid_dict = {(200, "OK"): "Success response"}  -пашет малышка
#invalid_dict = {[200, "OK"]: "Success response"} - будет вызывать TypeError
#6
required_scopes = {"read", "write"}
user_scopes = {"read", "write", "profile"}
has_all_scopes = required_scopes.issubset(user_scopes)
#7
expected_tags = {"api", "v2"}
actual_tags = {"api", "v1"}
extra_tags = actual_tags - expected_tags
#8
set1 = {"smoke", "regression"}
set2 = {"regression", "api"}
common_tags = set1 & set2
#9
def has_duplicates(my_list):
    return len(my_list) != len(set(my_list))
print(has_duplicates([1, 2, 3, 4, 5]))
print(has_duplicates([1, 2, 3, 2, 1]))
#10
data = [("user1", "pass1"), ("user2", "pass2"), ("user1", "pass1")]
unique_data_dict = dict.fromkeys(data)
unique_data_list = list(unique_data_dict.keys())

#Услов.операторы
#1
status_code = 401
if status_code == 200:
    print("OK")
else:
    print("Error")
#2
is_active = False
if not is_active:

#3

response_body = ""
if not response_body:

#4

status_code = 404
if status_code == 200:
    print("OK")
elif status_code == 404:
    print("Not Found")  # Not Found
elif status_code == 500:
    print("Server Error")
else:
    print("Unknown status")
#5
response_time = 1.2
if response_time > 1.0:
    print("Critical: Slow")  # Critical: Slow
elif response_time > 0.5:
    print("Warning: Slowish")
else:
    print("OK")
#6
env = "prod"
base_url = "prod_url" if env == "prod" else "stage_url"
#7
if response.get("data"):
    print("Data is present")
elif response.get("error"):
    print(f"Error occurred: {response['error']}")
else:
    print("No data and no error")
#8
def check_user_data(user):
    has_valid_id = "id" in user and isinstance(user["id"], int) and user["id"] > 0
    has_valid_email = "email" in user and "@" in str(user["email"])

    return has_valid_id and has_valid_email
#9
response = {"status": "success", "data": {"user": "Alice"}}
if response.get("status") == "success" and "data" in response:
    print("Valid successful response")  # Valid successful response
else:
    print("Invalid response")
#10
def categorize_response(response):
    if response is None or response == {}:
        return "EMPTY"
    elif "error" in response:
        return "ERROR"
    elif "data" in response:
        return "SUCCESS"
    else:
        return "UNKNOWN"



#цайкл
#1
browsers = ["chrome", "firefox", "edge"]
for browser in browsers:
    print(browser)

#2
for i in range(1, 6):
    print(f"Test run: {i}")
#3
payload = {"user": "test", "pass": "123"}
for key in payload.keys():
    print(key)
#4
response_times = [0.1, 0.5, 0.2, 1.1]
total_time = sum(response_times)
print(f"Total response time: {total_time}")
#5
test_statuses = ["pass", "fail", "pass"]
for status in test_statuses:
    if status == "fail":
        print("Build failed!")
        break
#6
user_data = ["Alice", None, "Bob"]
for user in user_data:
    if user is None:
        continue
#7
response = {"id": 1, "name": "Test"}
for key, value in response.items():
    print(f"Key: {key}, Value: {value}")
#8
users = [{"id": 1, "name": "A"}, {"id": 2, "name": "B"}]
for user in users:
#9
def find_user_by_id(users_list, user_id):
    for user in users_list:
        if user.get("id") == user_id:
            return user
    return None
#10
test_data = [["user1", "pass1"], ["user2", "pass2"]]
for row in test_data:
    for item in row:
        print(item)

