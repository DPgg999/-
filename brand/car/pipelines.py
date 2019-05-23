# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json

class CarPipeline(object):
    # def open_spider(self, spider):
    #     self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    #     self.databas = self.client['Cars_graph']
    #     self.tabls = self.databas['cars']
    #
    # def process_item(self, item, spider):
    #     dict0 = {
    #         # 'brand': item['brand'],
    #         'Brand_branch_names': item['Brand_branch_names'],
    #         'Brand_branch_hrefs': item['Brand_branch_hrefs'],
    #         'cars_name': item['cars_name'],
    #         'cars_addr': item['cars_addr']
    #     }
    #
    #     self.tabls.insert_one(dict0)
    #     return item
    #
    # def close_spider(self, spider):
    #     self.client.close()
    #
    def __init__(self):
        self.file = open('car.json', 'w')

    def process_item(self, item, spider):
        line = ""
        line += json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item
