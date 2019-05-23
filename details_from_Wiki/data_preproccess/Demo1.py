# -*- coding: utf-8 -*-
import json
import pandas as pd
car_name = open('Brand.txt' , 'w+')

data = pd.read_csv('Car.csv')

for i in range(1906):
    car_name.write(str(data['Brand_branch_names'][i]+"\n"))