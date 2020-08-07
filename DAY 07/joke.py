import requests

url = "https://sv443.net/jokeapi/v2/joke/Programming,Miscellaneous?blacklistFlags=religious&type=single"

response = requests.request("GET", url)

data = response.json()

print(data['joke'])