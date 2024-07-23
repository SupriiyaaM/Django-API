import requests

#create restapi endpoints 
#endpoint ="https://httpbin.org/status/200"
#endpoint = "https://httpbin.org/anything" 
endpoint = "http://127.0.0.1:8000/api/"


#requests.get() library is like using an API
# restAPIs are more web-based APIs

get_response = requests.post(endpoint, params={"abc" : 123} , json={"title": "title 1" , "content": "Hello World", "price": "11"}) #HTTP request
print(get_response.json()) #Source Code
#print(get_response.text) #raw text
#print(get_response.status_code)
