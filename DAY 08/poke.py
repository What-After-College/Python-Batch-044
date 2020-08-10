import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = requests.request("GET", url)
data = response.json()

print(data)