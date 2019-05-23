# -*- coding: utf-8 -*-
import scrapy
from Crawl_car.items import CrawlCarItem

class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ["http://www.baike.com"]
    file = open('Z:\项目\Car_\Car_Knowledge_Graph_A\Crawl_car\Crawl_car\spiders\car_name.txt', 'r').read()
    wordList = file.split()
    count = 0
    start_urls = []
    for i in wordList:
        url = "http://www.baike.com/wiki/"
        url = url + str(i)
        start_urls.append(url)
        count += 1
    # print(start_urls)
    # print(count) #3747
    def parse(self, response):
        deltail_count = 0
        item = CrawlCarItem()

        all_xpath_name = response.xpath(r'//div[@class="content-h1"]')
        for single_xpath in  all_xpath_name:
            name = single_xpath.xpath(r'.//h1/text()').extract_first()
            item['name'] = name

        all_xpath_key_value = response.xpath(r'//*[@id="datamodule"]/div[1]/table')
        for single_xpath in all_xpath_key_value:
            baseInfoKeyList = single_xpath.xpath(r'.//tr/td/strong/text()').extract()
            baseInfoValueList = single_xpath.xpath(r'.//tr/td/span/text()').extract()

            item['baseInfoKeyList'] = baseInfoKeyList
            item['baseInfoValueList'] = baseInfoValueList

        all_xpath_detail = response.xpath(r'//*[@id="content"]')
        for single_xpath in all_xpath_detail:
            detail = single_xpath.xpath(r'.//p/text()').extract()
            image_url = single_xpath.xpath(r'.//div[2]/a/@href').extract()

            item['detail'] = detail
            item['image_url'] = image_url

        yield item
