# -*- coding:utf-8 -*-
# Author:Jin Fei
'''
    需求：购物车
    1.启动程序后，让用户输入salary，然后打印商品列表
    2.允许用户根据商品编号购买商品
    3.用户选择商品后，付款时检测余额是否够，够就直接扣款，不够就提示
    4.可随时退出，退出时，打印已购商品和余额
'''
goods = [
    ("Mac Pro",15000),
    ("iPhone",5000),
    ("iWatch",4000),
    ("bycle",800),
    ("coffee",30)
]

salary = input("请输入您的salary")
buy = []
if salary.isdigit():
    print()
else:
    print("输入不是正确的格式")

