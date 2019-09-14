# -*- coding: utf-8 -*-
import scrapy
from autohome.items import AutohomeItem


class AutohomeSpiderSpider(scrapy.Spider):
    name = 'autohome_spider'
    # allowed_domains = ['club.autohome.com.cn']
    start_urls = ['https://club.autohome.com.cn/JingXuan/292/1']

    def parse(self, response):
        list = response.css(".pic-box")
        for image in list:
            img_name = image.css("a::attr(title)").extract_first()
            img_url = image.css("a::attr(href)").extract_first()
            img_url2 = 'https:'+str(img_url)
            # print(img_url2)
            next_page = response.css(".afpage::attr(href)").extract_first()
            if next_page:
                yield response.follow(next_page, callback=self.parse)

            yield scrapy.Request(img_url2, callback=self.downloadImage)

    def downloadImage(self, response):

            item = AutohomeItem()
            # item['img_name'] = response.css(".tz-figure img::attr(id)").extract() + response.css(".tz-picture img::attr(id)").extract()
            item['img_name'] = response.css('title::text').extract_first()
            item["img_urls"] = response.xpath('//div[@class="pic"]/img/@src').extract()[:6]+response.xpath('//div[@class="pic"]/img/@src9').extract()
            yield item


