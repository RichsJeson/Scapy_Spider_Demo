#!/usr/bin/env python
# encoding=utf-8
import scrapy
import re
from scrapy import Request, Selector

import json
import logging
from dj_spider.items.taobao_category_items import Category

# 商品列表
class ShopListSprider(scrapy.Spider):

    name = 'taobao_shop_list'

    start_urls = ['https://s.taobao.com/list?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&spm=a219r.lmn002.1000187.1&style=list']

    custom_settings = {

        'ITEM_PIPELINES': {
            'dj_spider.pipelines.taobao_shopitem_pipelines.CategoryPipelines': 301,
        },
        'SPIDER_MIDDLEWARES': {

        }
    }


    def __init__(self):
        self.filename = open("body.json", "w")
        pass

    # def start_requests(self):
    #      url = 'https://s.taobao.com/list?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&cat=16&seller_type=taobao&oetag=6745&source=qiangdiao&spm=a219r.lmn002.1000187.1'
    #      yield Request(url=url, callback=self.parse, meta={'shop_list': 4}, dont_filter=True)
    def parse(self, response):
        selector = Selector(response=response)
        for sel in selector.xpath('//script/text()'):
            self.log("=============================",level=logging.WARNING)
            desc = sel.extract()
            rsl = str(desc).replace(' ', '').replace("\n", "")
            #print("desc:" + desc)
            # match_re = re.match('{("\w*"):("\w*")*}', rsl)
            match_re = re.match('g_page_config[..]*', rsl)
            if(match_re):
                start=rsl.index("g_page_config")+len("g_page_config=");
                end=rsl.index("}};")+len("}};")-1;
                self.log(start)
                self.log(end)
                self.log(rsl[start:end],level=logging.WARNING)
                with open("content.json","w") as f:
                    f.write(rsl[start:end])
            # re.compile('g_page_config = {\w+\s+\w+')
            # re.finditer(str(desc,encoding='utf-8'))
        # print("zmo:"+jsContents)
        # service_fi_links = response.xpath('//*[@id="listsrp-itemlist"]/div/div/div').extract()
        # print('elements:',str(response.body, encoding = "utf-8")  )
        self.filename.write(str(response.body, encoding = "utf-8"))
        self.close()
        pass

