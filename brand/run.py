# -*- coding: UTF-8 -*-
# 作者 :冉照鹏
# 日期 :2019/5/9 21:24
#代码千万行，注释第一行， 
#命名不规范，师生两行泪。

from scrapy import cmdline
from car.spiders.cars import CarsSpider

name = CarsSpider.name
cmd = 'scrapy crawl {0} -o Car.csv'.format(name)

cmdline.execute(cmd.split())

