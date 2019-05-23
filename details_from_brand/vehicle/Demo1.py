# -*- coding: utf-8 -*-

list = []
car_brand = open('car_brand.txt','w+')
cnt = 1
with open('Brand.txt' , 'r') as f:
    for s in f:
        if s in list:
            continue
        else:
            car_brand.write(s)
            list.append(s)
            cnt += 1
