# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/1/21 11:59'
import re

import scrapy

import requests
import time
from lxml import etree

from snownlp import SnowNLP

from sci.items import SciItem, healthItem
from scrapy import Selector

class SjcSpider(scrapy.Spider):
    #爬虫名称
    name = 'health'
    # 爬取域范围
    allowed_domains = ['https://credit.wsjd.gov.cn/']
    # 开始爬取地址
    start_urls = ['https://credit.wsjd.gov.cn/portal/creditpublicity/0109000000?page=1&rows=10']
    #char_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



    def parse(self, response):

        data = response.body.decode()  # 获取响应内容
        # titles = re.findall(r'共有(.*?)条记录', data)  # 获取所有歌曲名
        #
        # title=titles[0].replace('共有','').replace('条记录','')
        #
        # pages=int(int(title)/20)+1

        #content=response.selector.xpath('//table[@id="5"]/tbody')#id="5"
        pages=response.selector.xpath('//*[@id="public-query"]/div[2]/div[2]/div/span/text()').extract_first()
        print (pages)
        page=int(re.findall(r'\d+', pages)[0])
        print(page)
        #page=10
        url='https://credit.wsjd.gov.cn/portal/creditpublicity/0109000000?page={}&rows=10'
        for i in range(page):
            i=i+1
            link=url.format(i)
            print(link)

            yield scrapy.Request(link, callback=self.parse_next, dont_filter=True)
            # t_response=scrapy.Request(link)
            # tmp = t_response.xpath('//*[@id="public-query"]/div[2]/div[2]/table/tbody/tr')
            # # 解析
            # for j in tmp:
            #     item = healthItem()
            #
            #     item['institutioni'] = j.xpath('.td[1]/a').extract_first()
            #     item['address'] = j.xpath('.td[2]').extract_first()
            #     item['business'] = j.xpath('.td[3]').extract_first()
            #     item['representative'] = j.xpath('.td[4]').extract_first()
            #     item['certificate'] = j.xpath('.td[5]').extract_first()
            #     item['date'] = j.xpath('.td[6]').extract_first()
            #     item['access_time'] = j.xpath('.td[7]').extract_first()
            #     print(item)
            #     yield item

            #yield scrapy.Request(link, callback=self.parse_next)
            #yield scrapy.Request(url, callback=self.parse_content, headers=headers)
       # content=content.selector.xpath(".//tr")//*[@id="5"]
        # html = response.xpath("/html/body")
        # tr = html.xpath(".//tr")  # 搜索body下的所有tr必须加上'.', 否则搜索的是整个文档的所有tr
        #pass
        #http://topj.lib.whu.edu.cn/search2.asp?searchtype=zk&sea=a&page=1
        #yield scrapy.Request(nexturl, callback=self.parse)
    def parse_next(self, response):
        # //*[@id="public-query"]/div[2]/div[2]/table/tbody
        tmp = response.xpath('//*[@id="public-query"]/div[2]/div[2]/table/tbody/tr')
        # 解析
        for i in tmp:
            item = healthItem()

            item['institution'] = i.xpath('./td[1]/a/text()').extract_first()
            item['address'] = i.xpath('./td[2]/text()').extract_first()
            item['business'] = i.xpath('./td[3]/text()').extract_first()
            item['representative'] = i.xpath('./td[4]/text()').extract_first()
            item['certificate'] = i.xpath('./td[5]/text()').extract_first()
            item['date'] = i.xpath('./td[6]/text()').extract_first()
            item['access_time'] = i.xpath('./td[7]/text()').extract_first()
            print(item)
            yield item


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
