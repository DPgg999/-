# -*- coding: utf-8 -*-
import scrapy
from vehicle.items import VehicleItem
class CarSpider(scrapy.Spider):
    name = 'Car'
    allowed_domains = ['baike.com']

    file_object = open('car_brand.txt', 'r').read()
    wordList = file_object.split()  # 获取词表

    start_urls = []

    for i in wordList:  ##生成url列表
        cur = "http://www.baike.com/wiki/"
        cur = cur + str(i)
        start_urls.append(cur)

    def parse(self, response):
        item = VehicleItem()
        title_list = response.xpath("//div[@class='w-990']")
        for tr in title_list:
            item["title"] = tr.xpath("./div[@class='l w-640']/div/h1/text()").extract_first()

        headline_list = response.xpath("//div[@class='place']")
        for tr in headline_list:
            item["headline"] = tr.xpath("./p/a/text()").extract()

        brief_list = response.xpath("//div[@id='unifyprompt']")
        for tr in brief_list:
            item["brief"] = tr.xpath("./div/p/text()[1]").extract()

        hyperlink_list = response.xpath("div[@id='content']")
        for tr in hyperlink_list:
            item["hyperlink"] = tr.xpath("./p/text()").extract()

        yield item