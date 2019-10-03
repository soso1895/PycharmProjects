# encoding uft-8

import requests
from bs4 import BeautifulSoup
import json


def get_page():
    url = "https://movie.douban.com/cinema/nowplaying/liaocheng/"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu \
        Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36 "
    }

    response = requests.get(url, headers=headers)
    text = response.text
    print(response.text)
    return text


def parse_page(text1):
    soup = BeautifulSoup(text1, 'html5lib')
    movies1 = []
    liList = soup.find_all("li", attrs={"data-category": 'nowplaying'})

    for li in liList:
        movie = {}
        title = li['data-title']
        score = li['data-score']
        release = li['data-release']
        actors = li['data-actors']
        img = li.find('img')
        thumbnail = img['src']
        movie['title'] = title
        movie['score'] = score
        movie['release'] = release
        movie['actors'] = actors
        movie['thumbnail'] = thumbnail
        movies1.append(movie)
    return movies1


def save_data(data):
    with open('douban.json', 'w', encoding='utf-8') as fp:
        json.dump(data, fp, ensure_ascii=False)


if __name__ == '__main__':
    text = get_page()
    movies = parse_page(text)
    save_data(movies)


