import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response= requests.get(endpoint, json={"product_id":123})
#print(get_response.headers)
#print(get_response.text)
#print(get_response.status_code)

print(get_response.json())
#print(get_response.status_code)
