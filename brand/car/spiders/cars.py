# -*- coding: utf-8 -*-
import scrapy
from car.items import CarItem
import copy
class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['price.pcauto.com.cn']
    start_urls = ['https://price.pcauto.com.cn/cars/q-ps8.html']

    def parse(self, response):
        item = CarItem()
        urls = "https://price.pcauto.com.cn"
        car_href = []

        row_1 = response.xpath('//div/div/div/div/div[@class="braRow-inner clearfix"]')
        for i,brand_ in enumerate(row_1):
            row_2 = brand_.xpath('./div[2]/div/div[1]')
            for Brand_branch_ in row_2:
                print(len(row_2))
                Brand_branch_name = Brand_branch_.xpath('./a/text()').extract_first()
                Brand_branch_href = Brand_branch_.xpath('./a/@href').extract_first()

                result_href = urls+Brand_branch_href
                item['Brand_branch_names'] = Brand_branch_name
                item['Brand_branch_hrefs'] = result_href

                print(Brand_branch_name, "========================", result_href)

                yield scrapy.Request(url=copy.deepcopy(result_href), callback=self.second_parse, meta={"meta_1": copy.deepcopy(item)},dont_filter=True)

    def second_parse(self,response):

        # print(response.url,"------------------------------")
        item = CarItem()
        meta_1 = response.meta['meta_1']
        urls = "https://price.pcauto.com.cn"

        item['Brand_branch_names'] = meta_1['Brand_branch_names']
        item['Brand_branch_hrefs'] = meta_1['Brand_branch_hrefs']

        # name = response.xpath('//*[@id="Jdoc"]/div/div[2]/div/div[3]/div[1]/p/text()').extract_first()

        # print(name,meta_1['Brand_branch_hrefs'])

        row = response.xpath('//*[@id="JlistTb"]/div/div[1]')
        count = 0
        for i in row:
            car_url = i.xpath('./p[1]/a/@href').extract_first()
            car_name = i.xpath('./p[1]/a/img/@title').extract_first()
            url_result = urls+car_url
            item['cars_addr'] = url_result
            item['cars_name'] = car_name

            print(item['Brand_branch_names'], "-------",len(row),"/",count+1,car_name)
            # print(url_result, car_name,"-----",item['Brand_branch_names'],item['Brand_branch_hrefs'])

            print(item['Brand_branch_names'],item['Brand_branch_hrefs'],item['cars_addr'],item['cars_name'])
            count+=1

            yield item






