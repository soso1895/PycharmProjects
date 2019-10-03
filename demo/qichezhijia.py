import requests
from bs4 import BeautifulSoup
import urllib.request
import os
from lxml import etree

DETAIL_URL_LIST = []
IMG_URL_LIST = []
HEADERS = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu \
            Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36 "
        }


def get_detail_url():

    url = "https://club.autohome.com.cn/JingXuan/104/1"
    response = requests.get(url, headers=HEADERS)
    text = response.content

    soup = BeautifulSoup(text, "lxml")
    # page_url_list = soup.find_all('div', attrs={'class': 'pic-box'})
    # for url in page_url_list:
    #     url.select('')
    page_urs_list = soup.select('.pic-box a')
    for url in page_urs_list:

        url = 'http:'+url['href']
        DETAIL_URL_LIST.append(url)


def get_img_url():
    url = "https://club.autohome.com.cn/bbs/thread/8b4ac5f8ac727913/82452459-1.html#pvareaid=102410"
    response = requests.get(url, headers=HEADERS)
    text = response.text

    # soup = BeautifulSoup(text, "lxml")
    # # soup.find_all 方法
    # img_url = soup.find_all('img', attrs={'onerror': 'tz.picNotFind(this)'})
    # for url in img_url:
    #     if url["name"] == "F06":
    #         url = 'http:'+url['src']
    #     else:
    #         url = 'http:'+url['src9']
    #     print(url)
    #     IMG_URL_LIST.append(url)
    # # soup.select方法
    # img_url = soup.select('div.pic img')
    # for url in img_url:
    #     print(url['name'])
    # xpath方法
    new_text = etree.HTML(text)
    img_url = new_text.xpath('//div[@class="pic"]/img/@src9')
    i = 0
    for url in img_url:
        i += 1
        print(url)
        print(i)


def download():
    while True:

        if len(IMG_URL_LIST) == 0:
            break
        else:
            img_url = IMG_URL_LIST.pop()
            split_list = img_url.split('/')
            filename = split_list.pop()
            path = os.path.join('images', filename)
            urllib.request.urlretrieve(img_url, filename=path)


if __name__ == '__main__':
    get_img_url()
    # download()
