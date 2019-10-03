
import requests
from lxml import etree
import json
from bs4 import BeautifulSoup

BASE_DOMAIN = "https://www.liaoxuefeng.com/wiki/1016959663602400"
HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu \
        Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36"
    }


def get_detail_urls(url):

    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspn']//a/@href")
    detail_urls = (lambda url: BASE_DOMAIN + url, detail_urls)
    return detail_urls


def parse_detail_page(url):
    movie = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title']//font[@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    screenshot = imgs[1]
    movie['cover'] = cover
    movie['screenshot'] = screenshot

    def parse_info(info, rule):
        return info.replace(rule, ""), strip()

    infos = zoomE.xpath(".//text()")
    for info in infos:
        if info.startswith("niandai"):
            info = parse_info(info, "niandai")
            movie['year'] = info
    return movie


def spider():
    base_url = "https://www.liaoxuefeng.com/wiki/1016959663602400/list_23_{}.html"
    movies = []
    for x in range(1, 8):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)


if __name__ == '__main__':
    spider()


