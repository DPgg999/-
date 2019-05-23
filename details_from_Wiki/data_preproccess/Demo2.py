# -*- coding: utf-8 -*-
import json
import pandas as pd
car_name = open('car_name.txt' , 'w+')

data = pd.read_csv('Car.csv')

for i in range(1906):
    car_name.write(str(data['cars_name'][i]+"\n"))










