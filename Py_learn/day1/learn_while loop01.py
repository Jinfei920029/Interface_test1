# -*- coding:utf-8 -*-
# Author:Jin Fei
# while loop
akon_age  = 28
count = 0
while count < 3:
    age_input = int(input("The akon's age:"))
    if age_input == akon_age:
        print("yes ,you got it !")
        break
    elif age_input < akon_age:
        print("too small")
    else:
        print("too old")
    count += 1
else:
    print("you have tried too many time , fuck off")
