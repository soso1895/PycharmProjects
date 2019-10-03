from bs4 import BeautifulSoup
import requests


def main():
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36",
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': None,
        'X-Requested-With': 'XMLHttpRequest',
        "Sec - Fetch - Mode": 'cors',
        'Sec - Fetch - Site': 'same - origin',
        'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh - CN, zh;q=0.9',
        'Connection': 'keep - alive',
        'Content - Length': '25',
        'Content - Type': 'application / x - www - form - urlencoded;charset=UTF-8',
        'Cookie': '''user_trace_token=20190902115645-ae7304be-cd35-11e9-a9a6-525400332722; _ga=GA1.2.844067037.1567396610; JSESSIONID=ABAAABAABEEAAJA9BD19CC92F4C1DF11FD90880E1BED616; WEBTJ-ID=20190903101158-16cf4e49b23172-07d0486b1f8898-250b4178-2073600-16cf4e49b307c7; index_location_city=%E5%8C%97%E4%BA%AC; X_HTTP_TOKEN=d675474b128f5f3f28177476513363fbda0d123917; TG-TRACK-CODE=search_code; SEARCH_ID=5a604c0cd5404397a36d0b773de6a68d'''
    }
    form_data = {
        'first': 'true',
        'pn': '1',
        'kd': 'python'
    }
    result = requests.post(url, headers=headers, data=form_data)
    print(result.content.decode('utf-8'))


if __name__ == '__main__':
    main()



