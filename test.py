import requests

# url = "http://localhost:8000/write_data"
# data = {
#     "phone": "89090000000",
#     "address": "текстовый адрес"
# }
#
# response = requests.post(url, json=data)

# url = "http://0.0.0.0:8000/write_data"
# data = {
#     "phone": "89252257315",
#     "address": "Самый новый)))"
# }

response = requests.put(url, json=data)

# url_create = "http://0.0.0.0:8000/write_data"
# data = {
#     "phone": "89252257315",
#     "address": "Мойадрес"
# }
#
# response_create = requests.post(url_create, json=data)

url = "http://0.0.0.0:8000/check_data/?phone=89252257315"


response = requests.get(url)

# print(response_create.status_code)
# print(response_create.json())

print(response.status_code)
print(response.json())


