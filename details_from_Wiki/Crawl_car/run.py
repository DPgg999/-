from scrapy import cmdline

name = 'car'
cmd = 'scrapy crawl {0} -o Car.csv'.format(name)

cmdline.execute(cmd.split())

