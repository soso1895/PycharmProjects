from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://club.autohome.com.cn/bbs/thread/e71194428c9f73ef/83066742-1.html#pvareaid=102410')
images = browser.find_elements_by_xpath('//img[@onerror="tz.picNotFind(this)"]')
print(len(images))
for image in images:
    print(image.get_attribute('src'))
browser.close()
