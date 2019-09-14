# -*- coding: utf-8 -*-
import scrapy
from angel.items import AngelItem

class AngelSpbeenSpider(scrapy.Spider):
    name = 'angel_spbeen'
    allowed_domains = ['angelimg.spbeen.com']
    start_urls = ['http://angelimg.spbeen.com/?mzt=on']

    def parse(self, response):
        # cookies = {
        #     "mzt": "CguKRKdORGkpQKUPskgDugbxvbpPcTUrRrYzSiVqTKkMDNjSXumwtnLrWrPtzGfCQasmQTHkKiswdWYyDYGCBLMDBYZBadUgPQUVRKhjQcnmwzWhgzOBSXQlNEqvVcdKwCpfIwZxbKSn"
        # }

        imgurl = response.css('.title a::attr(href)').extract()
        for u in imgurl:
            imgurl = str(u)
        imgname =response.css('.title a::text').extract()

        next_url = response.css('.ch.next::attr(href)').extract_first()
        if next_url is not None:
            yield response.follow(next_url, callback=self.parse)
        yield scrapy.Request(imgurl, callback=self.content)

    def content(self, response):
        item = AngelItem()
        item['name'] = response.css(".article h2::text").extract_first()
        item['ImgUrl'] = response.css(".content img::attr(src)").extract()
        item['referer'] = response.url
        yield item
        # print(item)
        next_url = response.css('.ch.next::attr(href)').extract_first()
        if next_url is not None:
            yield response.follow(next_url, callback=self.content)




