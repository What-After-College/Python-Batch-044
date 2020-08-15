import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

def get_id(n):
    df = pd.read_csv("links.csv")
    movies_ids = list(df.imdbId)
    start_index = 0
    end_index = n
    return movies_ids[start_index:end_index]

def scrap(id):
    url = "https://www.imdb.com/title/tt{}/".format(str(id).zfill(7))
    response = requests.request("GET", url)
    Soup = BeautifulSoup(response.text, "html.parser")
    info = Soup.find('script', attrs={"type":"application/ld+json"})
    info = info.string # info = str(info)[str(info).find('{'):-9]
    json_data = json.loads(info)
    movie = {
        "name" : json_data['name'],
        "genre" : json_data['genre'],
        "image" : json_data['image'],
        "description" : json_data['description']
    }
    return movie

def get_movies():
    ids = get_id(5)
    lis=[]
    for id in ids:
        movie_info = scrap(id)
        lis.append(movie_info)
    return lis


if __name__ == "__main__":
    ids = get_id(5)
    for id in ids:
        movie_info = scrap(id)
        print(movie_info)
    
    # scrap(114709)