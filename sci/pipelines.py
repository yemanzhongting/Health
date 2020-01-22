# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo

class SciPipeline(object):

    # def __init__(self):
    #     self.file = open('out.json', 'w')
    #
    # def process_item(self, item, spider):
    #     content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
    #     self.file.write(content)
    #
    #     return item

    def __init__(self):
        self.mongo_client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.db = self.mongo_client.disinfection_c  # 指定数据库
        self.connection = self.db.drink  # 指定数据集

    def process_item(self, item, spider):
        # print('##########')
        # print(item)
        # print('##########')
        # print(type(item))  <class 'items.MdpiItem'>
        # print('##########')
        self.connection.insert_one(dict(item))
        return item