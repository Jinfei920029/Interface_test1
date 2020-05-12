# -*- coding:utf-8 -*-
# Author:Jin Fei
import xlrd
import re

filename1 = r"C:\\Users\\A692297\\Desktop\\2019\\code_management\\report\\Cyclomatic Complexity.xlsx"

def Complexity(filename,ncol_index):
    sheet_index = 0
    data = xlrd.open_workbook(filename)
    sheet = data.sheet_by_index(sheet_index) #通过索引顺序获取工作表
    ncol_value = sheet.col_values(ncol_index)#获取某一列
    print(ncol_value)
    list1 = []
    for i in ncol_value:
        j = re.findall(r"\d+\.?\d*",i) #提取数字
        if j: # 存在值即为真
            list1.append(j[0])
    num = 0
    for k in list1:
        if float(k)>10:
            num = num + 1
    print(ncol_value[0],':',num)


Complexity(filename1,9)
Complexity(filename1,12)
