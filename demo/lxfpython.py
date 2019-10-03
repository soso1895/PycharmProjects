
import requests
from bs4 import BeautifulSoup
import json


def get_page():

    url = "https://www.liaoxuefeng.com/wiki/1016959663602400"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    text = response.text
    # print(text)
    return text


def parse_page(text):
    soup = BeautifulSoup(text, "lxml")
    liList = soup.find_all("li", attrs={"style": "margin-left:2em;"})
    # print(liList)
    for li in liList:
        dizhi = {}
        href = li['id'][4:]
        dizhi['title'] = "https://www.liaoxuefeng.com/wiki/1016959663602400/"+str(href)
        print(dizhi)
    # return movies


if __name__ == '__main__':
    text = get_page()
    parse_page(text)




