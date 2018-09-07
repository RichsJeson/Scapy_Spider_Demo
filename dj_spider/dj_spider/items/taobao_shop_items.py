# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ShopItem(scrapy.Item):
    print('ShopItem-----------')
    #s商品名称
    shop_name = scrapy.Field()
    #商品链接 钱夫人CHINSTUDIO春秋长袖v领碎花连衣裙女中长款韩版木耳边A字裙
    shop_link = scrapy.Field()
    #购买人数
    payers=scrapy.Field()
    #Merchant
    merchat=scrapy.Field()
    price=scrapy.Field()
    #address
    address=scrapy.Field()
    shop_images=scrapy.Field()
    print('shop_name：', shop_name)
    print('shop_link：', shop_link)
    print('payers：', payers)
    print('merchat：', merchat)
    print('price：', price)
    print('address：', address)


