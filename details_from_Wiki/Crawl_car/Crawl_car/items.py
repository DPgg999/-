# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlCarItem(scrapy.Item):

    name = scrapy.Field()
    baseInfoKeyList = scrapy.Field()
    baseInfoValueList = scrapy.Field()
    detail = scrapy.Field()
    image_url = scrapy.Field()

    pass
