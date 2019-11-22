# -*- coding:utf-8 -*-
# Author:Jin Fei
import os

count = 0

#basepath = os.path.abspath(__file__)
#folder = os.path.dirname(basepath)
#account_path = os.path.join(folder, 'account.txt')
#print(account_path) 绝对路径

while count < 3:
    uesrname = input("请输入用户名:")
    passwd = input("请输入密码:")
    if os.path.isfile("./account.txt"):  # 导入系统模块，判断输入username名称的文件是否存在
        f = open(file="./account.txt", mode='r', encoding='utf-8')
        account_data = eval(f.read())  # 文件存储的就是列表格式，读取的时候时字符串，需要转换成原来的格式了。
        f.close()
        for account in account_data:
            if account[2] == 1:
                if uesrname == account[0] and passwd == account[1]:
                    print("欢迎%s来到python世界"% uesrname)
                    break
                else:
                    count += 1
                    print("账号或密码错误，请重新输入，剩余输入次数%d" % (3 - count))
                    if count == 3:
                        print("你的用户即将被锁定")
            else:
                print("用户已经被锁定，请联系管理员解锁")