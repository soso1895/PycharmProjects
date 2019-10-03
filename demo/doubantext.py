#encoding utf-8


import requests
import json
from bs4 import BeautifulSoup


def get_page():

    url = "https://movie.douban.com/cinema/nowplaying/liaocheng/"

    headers = {
        "UserAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    text = response.text

    return text


def parse_page(text):
    soup = BeautifulSoup(text, "lxml")
    liList = soup.find_all('li', attrs={'data-category': 'nowplaying'})
    movies = []
    for li in liList:
        movie = {}
        title = li['data-title']
        score = li['data-score']
        star = li['data-star']
        release = li['data-release']
        region = li['data-region']
        actors = li['data-actors']
        movie['title'] = title
        movie['score'] = score
        movie['star'] = star
        movie['release'] = release
        movie['region'] = region
        movie['actors'] = actors
        movies.append(movie)

    return movies


def save_data(data):
    with open('doubantext.json', 'w', encoding='utf-8') as fp:
        json.dump(data, fp, ensure_ascii=False)


if __name__ == '__main__':
    text = get_page()
    movies = parse_page(text)
    save_data(movies)

