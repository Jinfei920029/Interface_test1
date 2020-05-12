# -*- coding:utf-8 -*-
# Author:Jin Fei
import os
import time
import re

fileName3 = "C:\\Users\\A692297\\Desktop\\2019\\Python Script\\total_code_line.txt"
fileName4 = 'C:\\Users\\A692297\\Desktop\\2019\\code_management\\report\\cloc2020-05-11-11_29_29.txt'
#读取 fileName3 自己得文件路径

def loadData(fileName):
    key = "Java"
    list_end = []
    with open(fileName, encoding='gb18030') as txtData:
        lines=txtData.readlines()
        for line in lines:
            if key in line:
                line=line.strip()#去除空行
                list = re.findall(r'\b\d+\b' , line)#取出数字
                list_end.append(list[-1])
    return list_end[-1]

print(loadData(fileName4))
