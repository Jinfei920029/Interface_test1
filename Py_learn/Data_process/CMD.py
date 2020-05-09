# -*- coding:utf-8 -*-
# Author:Jin Fei
import os
user_path1 = "C:\Users\A681549\Desktop\bsh_hcwxapp_api"
uesr_path2 = "C:\Users\A681549\Desktop\bsh_hcwxapp_api\src\main\java\com\zencloud\bsh"

def cmd1():
    try:
        cmd1 = ""
        cmd2 = "cpd.bat " + "--minimum-tokens 75 --files " +user_path1 + " >>" + "75 tokens test.txt"
        cmd = cmd1 + cmd2
        os.popen(cmd)
    except Exception as e:
        print("cloc tool fail:" + str(e))

def cmd2():
    try:
        cmd1 = ""
        cmd2 = "cloc-1.82.exe " + uesr_path2 + " >>" + "total_code_line.txt"
        cmd = cmd1 + cmd2
        os.popen(cmd2)
    except Exception as e:
        print("cloc tool fail:" + str(e))