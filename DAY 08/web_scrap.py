from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Constitution_of_India"

response = requests.request("GET", url)
data = response.text

soup = BeautifulSoup(data, "html.parser")

# print(soup.prettify())
# print(soup.title)
# print(soup.title.string)
# print(soup.title.parent.name)

# print(soup.find_all("p"))
# for i in soup.find_all("p"):
#     print(i.string)

# a = soup.find_all("a")
# print(a)

# print(soup.get_text())
