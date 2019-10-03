import re
from bs4 import BeautifulSoup
from lxml import etree
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36'
}


def get_code():
    response = requests.get('https://tieba.baidu.com/p/5743456239?pn=1', headers=headers).text
    return response


def use_xpath(code):
    new_code = etree.HTML(code)
    name = new_code.xpath('//li[@class="d_name"]/a/text()')
    for new in name:
        print(new.replace(' ', '').strip('\n'))
    content = new_code.xpath('//cc/div[@class="d_post_content j_d_post_content "]//text()')
    for new in content:
        print(new.strip())
        print('==='*20)


def use_soup(code):
    soup = BeautifulSoup(code, 'lxml')
    name = soup.select('li.d_name a')
    for new in name:
        print(new.get_text())

    content = soup.select('cc div')
    for new in content:
        print(new.get_text().strip())
        print('==='*20)


if __name__ == '__main__':
    code = get_code()
    use_xpath(code)

