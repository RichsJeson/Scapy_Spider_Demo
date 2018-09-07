#!/usr/bin/env python
# encoding=utf-8
import scrapy
from scrapy import Request, Selector
from dj_spider.items.taobao_category_items import Category


class TTLevelCategorySprider(scrapy.Spider):
    name = 'taobao_level_category'

    start_urls = ['https://www.taobao.com']

    def __init__(self):

        pass

    custom_settings = {

            'ITEM_PIPELINES': {
                'dj_spider.pipelines.taobao_category_pipelines.CategoryPipelines': 300,
            },
            'SPIDER_MIDDLEWARES': {

            }
        }

    def start_requests(self):
        url = 'https://www.taobao.com'
        yield Request(url=url, callback=self.parse, meta={'category_level': 3}, dont_filter=True)

    def parse(self, response):
        selector = Selector(response=response)
        service_fi_links = selector.xpath('.//div[@class="service-fi-links"]')
        for item in service_fi_links:
            service_panel = item.xpath('./div[@class="service-panel"]')
            for category_child in service_panel:
                category_parent = category_child.xpath("./h5/a[1]/text()").extract();
                category_parent_url = category_child.xpath("./h5/a[1]/@href").extract();
                category_childs = category_child.xpath("./p");
                # print('--------------------------------------------------')
                # print('获取主类目的数据', category_parent)
                # print('获取主类目的数据的连接地址：', category_parent_url)
                for item in category_childs:
                    category_child_item = item.xpath('./a/text()').extract()
                    category_child_item_url = item.xpath('./a/@href').extract()
                    for index in range(len(category_child_item)):
                        category = Category()
                        category['category_parent_name'] = category_parent;
                        category['category_parent_url'] = category_parent_url;
                        category['category_name'] = category_child_item[index];
                        category['category_url'] = category_child_item_url[index];
                        yield category
