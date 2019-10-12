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


def get_page(url="http://futures.hexun.com/2019-10-09/198804415_1.html"):


    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu \
        Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36"
    }
    while url is not None:
        response = requests.get(url, headers=headers)
        content = response.content
        new_code = etree.HTML(content)
        img_time = new_code.xpath('//div[@id="photoTime"]/text()')[0]
        img_time = int(img_time[13:-6])

        now_day = time.localtime().tm_mday
        # now_day = 30

        if now_day == img_time:

            img_url = new_code.xpath('//td[@valign="middle"]/img/@src')[0]
            img_name = new_code.xpath('//td[@valign="middle"]/img/@alt')[0]
            print(img_url, img_name)
            split_list = img_url.split('/')
            filename = img_name + split_list.pop()
            print(filename)
            # path = os.path.join('images', filename)
            path = '/home/ss/images/' + filename
            print(path)
            # break
            # urllib.request.urlretrieve(img_url, filename=path)
            urllib.request.urlretrieve(img_url, filename=path)
            next_page = new_code.xpath('//a[@class="pic_next"]/@href')[0]
            print(next_page)
            url = next_page
            time.sleep(0.5)
        else:
            break
        # return url


if __name__ == '__main__':
    get_page()




