# -*- coding:utf-8 -*-
# Author:Jin Fei
import os

if not os.path.exists('./data.txt'):#如果文件不存在就执行文件创建和写入，如果文件存在就不执行
    f = open('./data.txt','w')
    f.write('''{}''')
    f.close()

with open('./data.txt','r',encoding = 'utf-8') as f:
    menus = eval(f.read())#读取文件数据，并且转化为文件中的数据类型
    print("Welcome to online shopping mall".center(90,'*'))#center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
    menu = []#声明一个空列表来储存上一级菜单
    while True:
        dic = {}#声明一个空字典
        for index,good in enumerate(menus,1):#使用枚举函数遍历字典的键,#enumerate()有两个参数序列和起始索引。
            print(index,good)
            dic[index] = good #把序号作为字典的key，商品名称作为字典的value传入该字典中
        print('温馨提示：\n1.选择商品编号进入下一级菜单\n2.选择B或者b返回上一级菜单\n3.选择Q或者q退出商城')
        if type(menus) == list:
            choose = input('\033[31m请选择你要购买的商品编号：\033[0m').strip()
            if choose.isdigit():  # 判断输入的是否是纯数字
                if int(choose) <= len(menus):
                    print('您选择的%s已加入购物车！' % menus[int(choose) - 1])
                    print('\033[31m最后一级菜单，只能返回和退出！\033[0m')
                else:
                    print('out range')
            else:
                if choose == 'q' or choose == 'Q':
                    print('已退出购物商城！')
                    break
                elif choose == 'b' or choose == 'B':
                    menus = menu[-1]  # 把菜单赋值给列表的最后一个元素
                    menu.pop()  # 删掉列表的最后一个元素
                else:
                    print('error')
        else:
            choice = input('请选择您要购买的商品编号进入下一级菜单：').strip()
            if choice.isdigit():
                if int(choice) in dic.keys():
                    menu.append(menus)  # 把菜单添加到列表中
                    menus = menus[dic[int(choice)]]  # 重新赋值菜单
                else:
                    print('range out')
            else:
                if choice == 'B' or choice == 'b':
                    print('由于当前处于首层菜单，因此本次返回将退出程序！')
                    if len(menu) < 1: break
                    menus = menu[-1]  # 把菜单赋值给列表的最后一个元素
                    menu.pop()  # 删掉列表的最后一个元素
                elif choice == 'Q' or choice == 'q':
                    print('已退出购物商城！')
                    break
                else:
                    print('您的输入有误，请重新输入！')
