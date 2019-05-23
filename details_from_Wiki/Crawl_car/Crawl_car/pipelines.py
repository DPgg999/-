# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class CrawlCarPipeline(object):
    def __init__(self):
        self.file = open('car.json', 'w+')

    def process_item(self, item, spider):
        line = ""
        line += json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)

        return item
