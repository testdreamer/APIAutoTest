# _*_ coding : utf_8 _*_
# @Time : 17:19 
# @Author : 田霄汉
# @File : test_pandas
# @Project : APIAutoTest
# @User : Administrator


import pandas
import xlrd
import os
import xlwt
import yaml
import openpyxl

xlsPath = os.path.join(os.path.dirname(__file__), 'data/test_excel.xls')
xlsxPath = os.path.join(os.path.dirname(__file__), 'data/test_excel.xlsx')
csvPath = os.path.join(os.path.dirname(__file__), 'data/get_info.csv')

xlsRes = pandas.read_excel(xlsPath, sheet_name=0, header=0)
print(xlsRes)
xlsxRes = pandas.read_excel(xlsxPath, sheet_name=0, header=0)
print(xlsxRes)
csvRes = pandas.read_csv(csvPath)
print(csvRes.values)


