import requests

product_id = input("Please enter the ID of the data entry you want to delete below.\n")
try:
    product_id = int(product_id)  
except:
    product_id = None
    print(f"there is no data entry with that ID. Please try again.")
    
if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204) 