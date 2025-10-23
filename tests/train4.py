import json

base_url =  "https://vk.com"
base_url = base_url.strip().upper()
user_id = 12
price = 100.05
is_active = False


#url_get_users = base_url + "users/" + str(user_id)
list_url = url_get_users.split("/")
url_get_users = f"{base_url}users/{user_id}"
print(list_url)

response_data = {"id": 123, "name":"Denis","is_active":False}
assert response_data["is_active"] == is_active #False
none = None

user_data = json.loads(user_json)
print(f"Email ")