import requests
from bs4 import BeautifulSoup
import threading
import os
import urllib.request

BASE_PAGE_URL = "http://www.doutula.com/photo/list/?page="
PAGE_URL_LIST = []
FACE_URL_LIST = []
gLock = threading.Lock()

for x in range(1, 10):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)

#
# def download_image():
#     split_list = url.split('/')
#     filename = split_list.pop()
#     print(filename)
#     path = os.path.join('images', filename)
#     request.urlretrieve(url, filename=filename)


# def get_page():
#     url = "http://www.doutula.com/photo/list/?page=1"
#
#     headers = {
#         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu \
#         Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36"
#     }
#
#     response = requests.get(url, headers=headers)
#     content = response.content
#
#     soup = BeautifulSoup(content, 'lxml')
#     img_list = soup.find_all('img', attrs={'class': 'img-responsive lazy image_dta'})
#     for img in img_list:
#         url = img['data-original']
#         download_image(url)


def procuder():
    while True:
        gLock.acquire()
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu \
                    Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36 "
        }
        if len(PAGE_URL_LIST) == 0:
            gLock.release()
            break
        else:
            page_url = PAGE_URL_LIST.pop()
            # print(page_url)
            gLock.release()

            response = requests.get(page_url, headers=headers)
            content = response.content

            soup = BeautifulSoup(content, 'lxml')
            print(soup.text)
            img_list = soup.find_all('img', attrs={'class': 'img-responsive lazy image_dta'})
            print(img_list)
            gLock.acquire()
            for img in img_list:
                url = img['data-original']
                FACE_URL_LIST.append(url)
                # print(FACE_URL_LIST)
            gLock.release()


def customer():
    while True:
        gLock.acquire()
        if len(FACE_URL_LIST) == 0:
            gLock.release()
            continue
        else:
            face_url = FACE_URL_LIST.pop()
            gLock.release()
            split_list = face_url.split('/')
            filename = split_list.pop()
            print(filename)
            path = os.path.join('images', filename)
            urllib.request.urlretrieve(face_url, filename=path)


def main():
    for x in range(2):
        th = threading.Thread(target=procuder)
        th.start()
    for x in range(5):
        th = threading.Thread(target=customer)
        th.start()


if __name__ == '__main__':
    # get_page()
    # main()
    procuder()