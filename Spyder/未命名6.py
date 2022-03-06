# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 16:13:23 2022

@author: Molly Jack
"""
import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet('test')
ws.write(0, 0, '(0,0)')
ws.write(0, 1, '(0,1)')
ws.write(0, 2, '(0,2)')
wb.save('test.xls')