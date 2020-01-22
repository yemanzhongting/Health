# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SciItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    ISSN = scrapy.Field()
    CLASS= scrapy.Field()
    TOP=scrapy.Field()
    major=scrapy.Field()
    impact=scrapy.Field()
    #JCR刊名缩写	期刊名称	ISSN	所属大类(分区)	TOP期刊	所属小类(分区)	3年平均影响因子
    pass

class healthItem(scrapy.Item):
    # define the fields for your item here like:
    institution = scrapy.Field()
    address = scrapy.Field()
    business= scrapy.Field()
    representative=scrapy.Field()
    certificate=scrapy.Field()
    date=scrapy.Field()
    access_time=scrapy.Field()
    #JCR刊名缩写	期刊名称	ISSN	所属大类(分区)	TOP期刊	所属小类(分区)	3年平均影响因子
    pass
