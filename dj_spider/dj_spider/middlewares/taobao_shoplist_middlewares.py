#!/usr/bin/env python
# encoding=utf-8
from logging import getLogger

from scrapy.http import HtmlResponse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from dj_spider.items.taobao_shop_items import ShopItem
import json
#下载中间件，为了方便模拟点击淘宝界面上的ICON栏，

class CategoryMiddlewares(object):

    def __init__(self, timeout=None, service_args=[]):
        # self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.PhantomJS('/Users/richsjeson/compile/phatomjs/bin/phantomjs')
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)
        self.filename = open("shop_item.json", "w")

    def __del__(self):
        self.browser.close()


    def process_request(self, request, spider):
            """
                    用PhantomJS抓取页面
                    :param request: Request对象
                    :param spider: Spider对象
                    :return: HtmlResponse
                    """
            try:
                responseType=request.meta.get('shop_list')
                if  responseType==4:
                    self.browser.get(request.url)
                    shop_item=self.browser.find_elements_by_class_name('J_ItemListSKUItem')
                    for item in shop_item:
                        #执行数据提取的操作
                        items=item.find_element_by_class_name('J_IconMoreNew')
                        items_title=items.find_element_by_class_name('J_ClickStat')
                        print('item_title:----',items_title.text)
                        price=items.find_element_by_class_name('g_price')
                        payer=items.find_element_by_class_name('deal-cnt')
                        address=items.find_element_by_class_name('location')
                        merchat = items.find_element_by_class_name('shop')
                        items_image = item.find_elements_by_class_name('J_SKUItem')
                        print('item_image_url-----------------')
                        img_urls=[];
                        for items_image_url in items_image:
                            img_urls.append(items_image_url.get_attribute('data-src'))
                        shop_item=ShopItem();
                        shop_item['price']=price.text
                        shop_item['payers']=payer.text
                        shop_item['shop_name']=items_title.text;
                        shop_item['shop_link']=items_title.get_attribute('href')
                        shop_item['address']=address.text
                        shop_item['merchat']=merchat.text;
                        shop_item['shop_images']=img_urls;
                        text = json.dumps(dict(shop_item), ensure_ascii=False) + ",\n"
                        print('数据写入完成text：',text)
                        self.filename.write(text)
                        break
                    print('数据写入完成')
                    self.filename.close()
                    return HtmlResponse(url=request.url, request=request, body=self.browser.page_source, encoding='utf-8',
                                    status=200)
            except TimeoutException as e:
                    print('e:',e)
                    return HtmlResponse(url=request.url, status=500, request=request)
            pass



    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))