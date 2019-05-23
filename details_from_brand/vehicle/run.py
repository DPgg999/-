from scrapy import cmdline


name = 'Car'
cmd = 'scrapy crawl {0} -o car_brand.csv'.format(name)

cmdline.execute(cmd.split())

