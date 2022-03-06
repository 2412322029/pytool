# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:05:42 2022

@author: Molly Jack
"""

import csv
csvfile = open('test.csv', 'w')
writer = csv.writer(csvfile)
writer.writerow(['name', 'age'])
data = [
    ('张三', '25'),
    ('小明', '18')
]
writer.writerows(data)
csvfile.close()