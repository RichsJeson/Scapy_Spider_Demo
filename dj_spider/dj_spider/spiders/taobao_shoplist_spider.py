#!/usr/bin/env python
# encoding=utf-8
import scrapy
from scrapy import Request, Selector
from dj_spider.items.taobao_category_items import Category

# 商品列表
class ShopListSprider(scrapy.Spider):

    name = 'taobao_shop_list'

    start_urls = ['https://s.taobao.com/list?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&spm=a219r.lmn002.1000187.1']

    custom_settings = {

        'ITEM_PIPELINES': {
            'dj_spider.pipelines.taobao_shopitem_pipelines.CategoryPipelines': 301,
        },
        'SPIDER_MIDDLEWARES': {

        }
    }


    def __init__(self):

        pass

    def start_requests(self):
         url = 'https://s.taobao.com/list?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&spm=a219r.lmn002.1000187.1'
         yield Request(url=url, callback=self.parse, meta={'shop_list': 4}, dont_filter=True)
    def parse(self, response):
        pass

