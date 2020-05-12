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



