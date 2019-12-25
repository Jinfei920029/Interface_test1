# -*- coding:utf-8 -*-
# Author:Jin Fei
def fun1():
    '''函数'''
    print('fun1函数')
    return 0


def fun2():
    '''过程'''
    print('fun2过程')

x = fun1()
x2 = fun2()

print('fun1返回%s' %x)
print('fun2返回%s' %x2)
#过程是没有返回值的函数