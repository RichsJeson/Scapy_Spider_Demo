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


    insert_sql = 'insert into category(category_parentid,category_name,category_href,merchant_id,category_source,category_parent_name,category_parent_url) value(%s,%s,%s,%s,%s,%s,%s)'
   # __init__方法是可选的，做为类的初始化方法
    def __init__(self):
        self.filename = open("category.json", "w")
        self.dbargs = dict(
            host='111.230.63.83',
            db='dj_shop',
            user='root',
            passwd='bristua',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.db_conn = adbapi.ConnectionPool('pymysql', **self.dbargs)
        pass

    # process_item方法是必须写的，用来处理item数据
    def process_item(self, item, spider):
        # try:
        #     # 通过连接池执行具体的sql操作，返回一个对象
        #     query = self.db_conn.runInteraction(self.go_insert,self.insert_sql,item,spider)
        #     # 对错误信息进行提示处理
        #     query.addCallbacks(self.handle_error)
        #     text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        #     self.filename.write(text)
        # except Exception as e:
        #     print('error：',e)
        print('iten:',item['category_name'])
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.filename.write(text)
        return item

    # close_spider方法是可选的，结束时调用这个方法
    def close_spider(self, spider):
        self.filename.close()
        pass

    def go_insert(self,cursor,sql,category,spider):
        print('go_insert')
        try:
            cursor.execute(sql,(0,category['category_name'],category['category_url'],0,spider.start_urls,category['category_parent_name'],category['category_parent_url']))
        except Exception as e:
            print('error:',e)

    def handle_error(self,failure):
        # 打印错误
        if failure:
            print('e:',failure)
            pass

