#!/usr/bin/env python
# encoding=utf-8
from logging import getLogger

from scrapy.http import HtmlResponse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from dj_spider.conf.config import config

import time

#下载中间件，为了方便模拟点击淘宝界面上的ICON栏，

class CategoryMiddlewares(object):

    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.PhantomJS(config.phantomjs_path)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)
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
                responseType=request.meta.get('category_level')
                if  responseType==3:
                    print('TTLevelCategorySprider')
                    self.browser.get(request.url)
                    ul_element = self.browser.find_element_by_class_name('service-bd')
                    elements = ul_element.find_elements_by_class_name('a-all')
                    for index in elements:
                        ActionChains(self.browser).move_to_element(index).perform()
                        time.sleep(6)
                    pass
                    print('文件写入完成')
                    return HtmlResponse(url=request.url, request=request, body=self.browser.page_source, encoding='utf-8',
                                    status=200)
            except TimeoutException:
                    return HtmlResponse(url=request.url, status=500, request=request)
            pass



    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))
