# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import re


class ImagePipline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for img_url in item["img_urls"]:
            img_url = 'https:' + img_url
            print('-------------------image_url------------------------%s', img_url)
            yield Request(img_url, meta={'name': item['img_name']})

    #重命名的功能 重写此功能可以得到自己想要文件名称 否则就是uuid的随机字符串
    def file_path(self, request, response=None, info=None):
        #图片名称
        img_name = request.url.split('/')[-1]
        #图片分类的名称
        name = request.meta['name']
        #处理特殊字符串
        name = re.sub(r'[？\\*|“<>:/()0123456789]', '', name)
        #分文件夹存储
        filename = u'{0}/{1}'.format(name, img_name)
        return filename

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        #上面的表达式等于
        # for ok,x in results:
        #     if ok:
        #         print(x['path'])
        if not image_paths:
            raise DropItem('Item contains no images')
        item['img_urls'] = image_paths
        return item

