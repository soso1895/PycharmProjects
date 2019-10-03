
import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Bar
from pyecharts import options as opts
from example.commons import Faker
ALL_DATA = []


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'html5lib')
    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({'city': city, 'min_temp': int(min_temp)})
            # print({'city': city, 'min_temp': int(min_temp)})


def main():
    urls = [
        "http://www.weather.com.cn/textFC/hb.shtml",
        "http://www.weather.com.cn/textFC/db.shtml",
        "http://www.weather.com.cn/textFC/hd.shtml",
        "http://www.weather.com.cn/textFC/hz.shtml",
        "http://www.weather.com.cn/textFC/hn.shtml",
        "http://www.weather.com.cn/textFC/xb.shtml",
        "http://www.weather.com.cn/textFC/xn.shtml",
        "http://www.weather.com.cn/textFC/gat.shtml",
    ]
    for url in urls:

        parse_page(url)
    ALL_DATA.sort(key=lambda data: data['min_temp'])
    # print(ALL_DATA)

    data = ALL_DATA[:10]
    # cities = list((lambda x: x['city'], data))
    # temps = list(map(lambda x: x['min_temp'], data))
    # chart = Bar()
    # chart.add_yaxis('', cities, temps)
    # chart.render('temperature.html')
    print(data)


if __name__ == '__main__':
    main()




