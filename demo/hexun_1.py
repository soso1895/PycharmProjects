import requests
from bs4 import BeautifulSoup
import os
import urllib.request
from lxml import etree
import time


def get_page(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu \
        Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    content = response.content
    return content


def parse_page(content):

    new_code = etree.HTML(content)

    img_url = new_code.xpath('//td[@valign="middle"]/img/@src')[0]
    img_name = new_code.xpath('//td[@valign="middle"]/img/@alt')[0]

    next_page = new_code.xpath('//a[@class="pic_next"]/@href')[0]

    img_time = new_code.xpath('//div[@id="photoTime"]/text()')[0]
    img_time = int(img_time[13:-6])

    return img_time, img_name, img_url, next_page


def download_image(img_url, img_name):

    split_list = img_url.split('/')
    filename = img_name + split_list.pop()
    print(filename)
    # path = os.path.join('images', filename)
    path = '/home/ss/images/' + filename
    print(path)
    # break
    # urllib.request.urlretrieve(img_url, filename=path)
    urllib.request.urlretrieve(img_url, filename=path)


def main():
    url = "http://futures.hexun.com/futurespic/"
    now_day = time.localtime().tm_mday
    content = get_page(url)
    a = parse_page(content)
    download_image()
    pass


if __name__ == '__main__':
    get_page()




