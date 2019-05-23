# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # brand = scrapy.Field()
    Brand_branch_names = scrapy.Field()
    Brand_branch_hrefs = scrapy.Field()
    cars_name = scrapy.Field()
    cars_addr = scrapy.Field()

    pass
