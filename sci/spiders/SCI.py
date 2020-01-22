# encoding: utf-8
'''
@sci    @SCI 
@Administrator    @2020/1/15  @13:36 
@PyCharm
'''
import re

import scrapy

import requests
import time
from lxml import etree

from snownlp import SnowNLP

from sci.items import SciItem
from scrapy import Selector

class SjcSpider(scrapy.Spider):
    #爬虫名称
    name = 'sci'
    # 爬取域范围
    allowed_domains = ['topj.lib.whu.edu.cn']
    # 开始爬取地址
    start_urls = ['http://topj.lib.whu.edu.cn/search2.asp?searchtype=zk&sea=a&page=1']
    char_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def parse(self, response):

        data = response.body.decode()  # 获取响应内容
        titles = re.findall(r'共有(.*?)条记录', data)  # 获取所有歌曲名

        title=titles[0].replace('共有','').replace('条记录','')

        pages=int(int(title)/20)+1

        content=response.selector.xpath('//table[@id="5"]/tbody')#id="5"
       # content=content.selector.xpath(".//tr")//*[@id="5"]
        # html = response.xpath("/html/body")
        # tr = html.xpath(".//tr")  # 搜索body下的所有tr必须加上'.', 否则搜索的是整个文档的所有tr
        pass
        #http://topj.lib.whu.edu.cn/search2.asp?searchtype=zk&sea=a&page=1
        #yield scrapy.Request(nexturl, callback=self.parse)

#感觉还可以的，翻页，请求next_page
#coding:utf-8
# import scrapy
# from freebuf2.items import Freebuf2Item
# import time
# from scrapy.crawler import CrawlerProcess
#
# class freebuf2Spider(scrapy.Spider):
#     name ='freebuf2'
#     allowed_domains = []
#
#     start_urls = ["http://www.freebuf.com/"]
#
#     def parse(self, response):
#
#         for link in response.xpath("//div[contains(@class, 'news_inner news-list')]/div/a/@href").extract():
#
#
#             yield scrapy.Request(link, callback=self.parse_next)#这里不好理解的朋友，先去看看yield的用法。我是按协程（就是中断执行）理解的，感觉容易理解。
#
#
#
#         next_url = response.xpath("//div[@class='news-more']/a/@href").extract()#找到下一个链接，也就是翻页。
#
#
#
#         if next_url:
#
#             yield scrapy.Request(next_url[0],callback=self.parse)
#
#     def parse_next(self,response):
#         item = Freebuf2Item()
#         item['title'] = response.xpath("//h2/text()").extract()
#         item['url'] = response.url
#         item['date'] = response.xpath("//div[@class='property']/span[@class='time']/text()").extract()
#         item['tags'] = response.xpath("//span[@class='tags']/a/text()").extract()
#
#         yield item