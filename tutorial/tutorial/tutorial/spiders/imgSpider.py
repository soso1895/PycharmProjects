# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import ImageItem


class ImgspiderSpider(scrapy.Spider):
    name = 'imgSpider'
    allowed_domains = ['www.mm131.net']
    start_urls = [
                'https://www.mm131.net/xinggan/list_6_31.html',
                'https://www.mm131.net/qingchun/',
                'https://www.mm131.net/xiaohua/',
                'https://www.mm131.net/chemo/',
                'https://www.mm131.net/qipao/',
                'https://www.mm131.net/mingxing/'
                ]

    def parse(self, response):
        list = response.css(".list-left dd:not(.page)")
        for image in list:
            image_name = image.css("a::text").extract_first()
            image_url = image.css("a::attr(href)").extract_first()
            image_url2 = str(image_url)
            # print(image_url2)
            next_page = response.css(".page-en:nth-last-child(2)::attr(href)").extract_first()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)

            #下载图片
            yield scrapy.Request(image_url2, callback=self.downloadImage)

    def downloadImage(self, response):
        item = ImageItem()
        item['image_name'] = response.css(".content h5::text").extract_first()

        item['image_urls'] = response.css(".content-pic img::attr(src)").extract()
        print('---------------image_urls---------', item['image_urls'])
        #防盗链:referer 从那个页面过来 没有来源就图片就会被重定向 解决办法在请求头中添加 headers={"referer":referer}
        # 解决防盗链的最根本的就是告诉访问的资源的请求来自本站
        item['referer'] = response.url
        yield item
        next_url = response.css(".page-ch:last-child::attr(href)").extract_first()
        if next_url is not None:
            yield response.follow(next_url, callback=self.downloadImage, dont_filter=True)

