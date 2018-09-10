# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import pymysql
from twisted.enterprise import adbapi


# 添加字段元素的值

class CategoryPipelines(object):

   # __init__方法是可选的，做为类的初始化方法
    def __init__(self):
        self.filename = open("shopitem.json", "w")
        pass

    # process_item方法是必须写的，用来处理item数据
    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.filename.write(text)
        return item

    # close_spider方法是可选的，结束时调用这个方法
    def close_spider(self, spider):
        self.filename.close()
        pass


