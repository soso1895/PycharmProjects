import requests
from bs4 import BeautifulSoup
import os
import urllib.request
from lxml import etree
import time


# def download_image():
#     split_list = url.split('/')
#     filename = split_list.pop()
#     print(filename)
#     path = os.path.join('images', filename)
#     request.urlretrieve(url, filename=filename)


def get_page(url="http://futures.hexun.com/2019-09-30/198735397_1.html"):


    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu \
        Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36"
    }
    while url is not None:
        response = requests.get(url, headers=headers)
        content = response.content
        new_code = etree.HTML(content)
        img_url = new_code.xpath('//td[@valign="middle"]/img/@src')[0]
        img_name = new_code.xpath('//td[@valign="middle"]/img/@alt')[0]
        print(img_url, img_name)
        split_list = img_url.split('/')
        filename = img_name + split_list.pop()
        print(filename)
        path = os.path.join('images', filename)
        urllib.request.urlretrieve(img_url, filename=path)
        next_page = new_code.xpath('//a[@class="pic_next"]/@href')[0]
        print(next_page)
        url = next_page
        time.sleep(0.5)
        # return url


if __name__ == '__main__':
    get_page()




