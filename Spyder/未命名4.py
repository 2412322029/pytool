# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:03:10 2022

@author: Molly Jack
"""

import openpyxl
wb=openpyxl.load_workbook('bg.xlsx')
sheet=wb.worksheets[0]
for row in sheet.iter_rows():
	for cell in row:
		print(cell.coordinate, cell.value)