import requests

endpoint = "http://127.0.0.1:8000/api/products/4/update/"

data = {
    'title': 'this is the updated title!',
    'content' : 'this is the updated content',
}

get_response = requests.put(endpoint, json = data)
print(get_response.json()) 