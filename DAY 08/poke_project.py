import requests
from matplotlib import pyplot as plt

def save_img(response2):
    with open("poke.png","wb") as f:
        for item in response2.iter_content():
            f.write(item)


def show_img():
    img_data = plt.imread("poke.png")
    plt.imshow(img_data)
    plt.show()


def url_builder(name):
    return "https://api.pokemontcg.io/v1/cards?name=" + name


if __name__ == "__main__":
    name = input("Enter the name of pokemon : ")
    url = url_builder(name)
    
    response = requests.request("GET", url)
    response_data = response.json()

    img_url = response_data["cards"][0]["imageUrl"]
    response2 = requests.request("GET",img_url)

    save_img(response2)
    show_img()