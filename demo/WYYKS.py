
import requests
from bs4 import BeautifulSoup
import json


def get_page():

    url = "https://study.163.com/course/courseMain.htm?courseId=1006385066"

    headers = {
        "UserAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    text = response.text
    print(text)
    return text


def parse_page(text):
    soup = BeautifulSoup(text, "lxml")
    liList = soup.find_all("div", attrs={"class": "section"})
    print(liList)
    # for li in liList:
    #
    #     print(li)

    # return movies


if __name__ == '__main__':
    text = get_page()
    parse_page(text)
