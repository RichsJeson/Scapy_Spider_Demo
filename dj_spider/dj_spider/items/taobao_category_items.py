# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Category(scrapy.Item):
    print('category_-----------')

    #类目名称
    category_name = scrapy.Field()
    # 类目名url
    category_url = scrapy.Field()
    category_parent_name=scrapy.Field()
    category_parent_url=scrapy.Field()
    print('category_name:',category_name)
    print('category_url:', category_url)
    print('category_parent_name:', category_parent_name)
    print('category_parent_url:', category_parent_url)