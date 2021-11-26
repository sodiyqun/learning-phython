# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 02:22:46 2021

@author: sodiyqun
"""

# def ty_xisobla(ism, yosh):
#     '''Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini 
#     hisoblaydigan funksiya'''
#     print(f"{ism.title()} {2021-yosh} yilda tug'ilgan")
    
# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))
# ty_xisobla(ism, yosh)


# def kvkub_xioblovchi(son):
#     '''Foydalanuvchidan son olib, uning kvadrati va kubini konsolga 
#     chiqaruvchi funksiya'''
#     print(f"\n{son}'ning kvadrati {son**2}'ga, kubi {son**3}'ga teng")
    
# son = int(input("Istalgan butun son kiriting: "))
# kvkub_xioblovchi(son)


# def tj_top(son):
#     '''Foydalanuvchidan son olib, son juft yoki toqligini konsolga 
#     chiqaruvchi funksiya'''
#     if son%2 == 0:
#         print("Juft son")
#     else:
#         print("Toq son")
        
# son = int(input("Son kiriting: "))
# tj_top(son)


# def tenglik_top(x, y):
#     '''Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga 
#     chiqaruvchi funksiya'''
#     if x>y:
#         print(f"{x} soni {y} sonidan katta")
#     elif x<y:
#         print(f"{y} soni {x} sonidan katta")
#     else:
#         print(f"{x} va {y} sonlar bir biriga teng")
        
# x = float(input("Istalgan son kiring: "))
# y = float(input("Istalgan son kiring: "))
# tenglik_top(x, y)

# def kv_top(x, y=2):
#     '''Foydalanuvchidan x va y sonlarini olib, x'ni y'darajasini 
#     konsolga chiqaruvchi funksiya'''
#     print(f"\nNatija: {x**y}")
    
# x = float(input("Istalgan son kiriting: "))
# # y = float(input("Istalgan son kiriting: "))
# # kv_top(x, y)
# kv_top(x)


# def bolinish_alomatlari(son):
#     '''Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan 
#     sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya'''
#     for n in range(2,11):
#         if son%n == 0:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")
            
# son = int(input("Istalgan butun son kiriting: "))
# bolinish_alomatlari(son)