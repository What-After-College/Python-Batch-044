import requests

url = "https://currencyapi.net/api/v1/rates?key=NXtUyotjncqJie5GKVEjlBi6FYfjgQuQyjjL&base=USD"

response = requests.request("GET",url)
data = response.json()
print(data["rates"]["INR"])