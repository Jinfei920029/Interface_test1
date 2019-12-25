# -*- coding:utf-8 -*-
# Author:Jin Fei
name = ['A','B','C','D']
print(name[1:3])#切片
print(name[-1])#切片
print(name[1:])
name.append('E')#列表后面追加
print(name)
name.insert(1,'e')#列表插入
print(name)
name[1]='E'#列表修改
print(name)
del name[1]#列表删除
print(name)
name.pop(4)#pop()默认删除最后一个，给位置删除指定位置
print(name)
print(name.index('C'))
name.reverse()#翻转
print(name)
name.sort()#排序
print(name)
name2 = ['a','b','c']
name.extend(name2)#列表合并
print(name)
print('a'.islower())
print('A'.isupper())
print('+'.join(name2))#Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
print('  \nabcd'.strip())#去掉空格和回车
