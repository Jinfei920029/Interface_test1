# -*- coding:utf-8 -*-
# Author:Jin Fei
import os

if not os.path.exists('./data.txt'):#如果文件不存在就执行文件创建和写入，如果文件存在就不执行
    f = open('./data.txt','w')
    f.write('''{}''')
    f.close()

with open('./data.txt','r',encoding = 'utf-8') as f:
    data = eval(f.read())#读取文件数据，并且转化为文件中的数据类型
    print("Welcome to online shopping mall".center(90,'*'))#center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
    menu = []#声明一个空列表来储存上一级菜单