# -*- coding:utf-8 -*-
# Author:Jin Fei
import os
import time
import re

now = str(time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime()))
user_path1 = "C:\\Users\\A692297\\Desktop\\2019\\code_management"
report_path1 = "C:\\Users\\A692297\\Desktop\\2019\\code_management\\report"
report_name1 = 'cloc' + now + '.txt'
report_name2 = 'tokens_' + now + '.txt'


def cmd1():
    try:
        cmd1 = "cd C:\\Users\\A692297\\Desktop\\2019\\code_management"
        cmd2 = "cloc-1.82.exe " + user_path1 +"\\bsh_hcwxapp_api\\src\\main\\java\\com\\zencloud\\bsh" + " >>" + report_path1 + "\\" + report_name1
        cmd = cmd1 + '&&' + cmd2
        os.popen(cmd)
    except Exception as e:
        print("cloc tool fail:" + str(e))

def cmd2():
    try:
        cmd1 = "cd C:\\Users\\A692297\\Desktop\\2019\\code_management\\pmd-bin-6.20.0\\bin"
        cmd2 = "cpd.bat --minimum-tokens 6 --files " + user_path1 +"\\bsh_hcwxapp_api" + " >>" + report_path1 + "\\" + report_name2
        #cmd2 = "dir" + " >>" + report_path1 + "\\" + report_name2
        cmd = cmd1 + '&&' + cmd2
        os.popen(cmd)
    except Exception as e:
        print("tokens tool fail:" + str(e))

cmd1()
cmd2()



time.sleep(10)



report1_psth = "C:\\Users\\A692297\\Desktop\\2019\\code_management\\report\\" + report_name2
report2_path = "C:\\Users\\A692297\\Desktop\\2019\\code_management\\report\\" + report_name1
fileName1 = report1_psth
fileName2 = report2_path
#读取 fileName3 自己得文件路径

def loadData1(fileName):
    key = "Found a"
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

line1 = loadData1(fileName1)
line2 = get_codeline(fileName2)
code_repetion_rate = int(line1)/int(line2)
print('Code_repetion_rate:'+ str(code_repetion_rate)+'\n','Data1:'+ str(loadData1(fileName1))+'\n','Data2:'+ str(get_codeline(fileName2)))


