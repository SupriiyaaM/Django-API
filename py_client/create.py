import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    'title': "This is the CreateAPIView using Mixin!",
    'price': 120.00
}
get_response = requests.post(endpoint, json = data)
print(get_response.json()) 