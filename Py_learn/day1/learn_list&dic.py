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