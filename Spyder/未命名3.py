# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 15:57:24 2022

@author: Molly Jack
"""

import csv
with open('csv.csv')as f:
   f_csv = csv.reader(f)
   for row in f_csv:
        print(row)