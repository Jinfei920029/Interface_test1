# -*- coding:utf-8 -*-
# Author:Jin Fei
import os
import time
import re
'''
report1_psth = "C:\\Users\\A692297\\Desktop\\2019\\Python Script\\code_20200327.txt.txt"
report2_path = "C:\\Users\\A692297\\Desktop\\2019\\Python Script\\total_code_line.txt"
fileName1 = report1_psth
fileName2 = report2_path
#读取 fileName3 自己得文件路径

def loadData1(fileName):
    key = "Found"
    with open(fileName, encoding='gb18030') as txtData:
        lines=txtData.readlines()
        num = 0
        for line in lines:
            if key in line:
                line=line.strip()#去除空行
                list = re.findall(r'\b\d+\b' , line)#取出数字
                print(list)
                print(list[0])
                num = num + int(list[0])
    return num

def get_codeline(fileName):
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
'''
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

loadData3(fileName3)
