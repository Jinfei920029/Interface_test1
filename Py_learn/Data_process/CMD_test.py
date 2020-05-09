# -*- coding:utf-8 -*-
# Author:Jin Fei
import os
user_path1 = "C:\\Users\\A692297\\Jinfei\\software\\PyCharm_project\\Py_learn\\Data_process.py"
#uesr_path2 = "C:\\Users\\A681549\\Desktop\\bsh_hcwxapp_api\\src\\main\\java\\com\\zencloud\\bsh"

def cmd1():
    try:
        print("hello")
        cmd1 = 'cd C:/Users/A692297/Jinfei/software/PyCharm_project/Py_learn/Data_process'
        cmd2 = 'python .\Data_process.py >> result.txt'
        cmd = cmd1 + '&&' + cmd2
        os.popen(cmd)
    except Exception as e:
        print("cloc tool fail:" + str(e))

cmd1()

'''def cmd2():
    try:
        cmd2 = "cloc-1.82.exe " + uesr_path2 + " >>" + "./total_code_line.txt"
        os.popen(cmd2)
    except Exception as e:
        print("cloc tool fail:" + e.message)'''