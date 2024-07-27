import requests

endpoint = "http://127.0.0.1:8000/api/products/"

headers = {'Authorization': 'Bearer 6aea8b705351327da06605040a34acda7da698d5'}
data = {
    'title': "This is the another Product to check login/logout!",
    'price': 120.00
}
get_response = requests.post(endpoint, json = data, headers=headers)
print(get_response.json()) 