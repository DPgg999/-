# -*- coding: utf-8 -*-
import re

file = open('car_brand_label.txt' , 'w+')

count = 1
with open('car_brand.txt' , 'r') as f:
    for i in f:
        file.write(re.sub('\n' , ' ' , i) + str(count) + '\n')
        count += 1