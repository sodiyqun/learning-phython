# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 20:14:31 2021

@author: sodiyqun
"""

# try:
#     x = int(input("son kiriting: "))
#     y = int(input("yana bir son kiriting: "))
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# except ValueError:
#     print("Butun son emas")
# except:
#     print("Xato yuz berdi!")
# else:
#     print(x, "/", y, '=', x/y)




while True:
    x = input("x ni kiriting: ")
    if x.isdigit():
        x = int(x)
        break
    else:
        print("butun son emas")
        continue
    
while True:
    y = input("y ni kiriting: ")
    if y.isdigit():
        y = int(y)
    else:
        print("butun son emas")
        continue
    
    if y == 0:
        print("y 0 bo'lishi mumkin emas!")
        continue
    else:
        print(x, "/", y, "=", x / y)
        break