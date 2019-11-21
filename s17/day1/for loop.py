# -*- coding:utf-8 -*-
# Author:Jin Fei
# while loop

Akon_age = 23
for i in range(3):
    age = int(input("guess akon's age:"))
    if age == Akon_age:
        print("yes ,you got it")
        break
    elif age < Akon_age :
        print("too young")
    else:
        print("too large")
else:
    print("you have tried too many times ,fuck off")