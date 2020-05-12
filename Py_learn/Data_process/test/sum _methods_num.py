# -*- coding:utf-8 -*-
# Author:Jin Fei
import os
import time
import re

report3_path = "C:\\Users\\A692297\\Desktop\\2019\\code_management\\report\\sum _methods_num.txt"
fileName3 = report3_path

def loadData3(fileName):
    key = "methods is"
    with open(fileName, encoding='gb18030') as txtData:
        lines=txtData.readlines()
        num = 0
        for line in lines:
            if key in line:
                line=line.strip()#去除空行
                list = re.findall(r'\b\d+\b' , line)#取出数字
                print(list)
                num = num + int(list[0])
    return num

sum_methods_num = loadData3(fileName3)
print('sum _methods_num: ',sum_methods_num)