import requests
import json

BASE_URL = "http://127.0.0.1:5000"

# GET /hello - welcome message
print("GET /hello:")
print(requests.get(f"{BASE_URL}/hello").json())

# GET /data/3 - returns one car with ID of 3
print("\nGET /data/3:")
print(requests.get(f"{BASE_URL}/data/3").json())

# GET /data - returns all the cars
print("\nGET /data:")
print(requests.get(f"{BASE_URL}/data").json())

# POST /data - add a new car
new_car = {"CarName": "toyota model 3", "price": 40000}
print("\nPOST /data:")
print(requests.post(f"{BASE_URL}/data", json=new_car).json())

# GET /data again - new car was added
print("\nGET /data after POST:")
print(requests.get(f"{BASE_URL}/data").json())
