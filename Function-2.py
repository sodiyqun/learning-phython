# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 21:57:12 2021

@author: sodiyqun
"""

# def info_yeg(name, surname, year, location, email='', phone=''):
#     info = {
#         'ism': name,
#         'familiya': surname,
#         'tyil': year,
#         'yosh': 2021-year,
#         'shahar': location,
#         'e-pochta': email,
#         'raqam': phone
#         }
#     return info

# print("Ma'lumotlarni kiriting")
# person = {}
# ismi = input("Ismingiz: ")
# familiyasi = input("Familiyangiz: ")
# tyili = int(input("Tug'ilgan yilingiz: "))
# shahri = input("Tug'ilgan shahringiz: ")
# pochatasi = input("Elektron pochtangiz: ")
# raqami = input("Telefon raqamingiz: ")
# person = info_yeg(ismi, familiyasi, tyili, shahri, pochatasi, raqami)
# print(person, end='')


# def info_yeg(name, surname, year, location, email='', phone=''):
#     info = {
#         'ism': name,
#         'familiya': surname,
#         'tyil': year,
#         'yosh': 2021-year,
#         'shahar': location,
#         'e-pochta': email,
#         'raqam': phone
#         }
#     return info
# print("Userlarni qo'shamiz.")
# users = []
# while True:
#     print("\nMa'lumotlarni kiriting", end='')
#     ismi = input("Ismi: ")
#     familiyasi = input("Familiyasi: ")
#     tyili = int(input("Tug'ilgan yili: "))
#     shahri = input("Tug'ilgan shahri: ")
#     pochatasi = input("Elektron pochtasi: ")
#     raqami = input("Telefon raqami: ")
#     users.append(info_yeg(ismi, familiyasi, tyili, shahri, pochatasi, raqami))
#     valid = input("Yana qo'shasizmi? (Ha/Yo'q)\n>>> ").lower()
#     if valid == "yo'q" or valid == "y":
#         break

# for user in users:
#     if user['raqam']:
#         number = user['raqam']
#     else:
#         number = "kiritilmagan"
#     print(f"{user['ism'].title()} {user['familiya'].title()}, {user['yosh']} yoshda, telefon raqami: {number}.")


# def kat_aniqla(x, y, z):
#     max = x
#     if y > max:
#         max = y
#     elif z > max:
#         max = z
#     return max
# print(kat_aniqla(8, 5, 7))


# def ainfo(r, pi=3.14):
#     aylana = {
#         'radius': r,
#         'diametr': r*2,
#         'perimetr': r*2*pi,
#         'yuza': r**2*pi
#         }
#     return aylana


# def tubtop(min, max):
#     tubsonlar = []
#     for n in range(min, max+1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for s in range(2, n):
#                 if n%s == 0:
#                     tub = False
#         if tub:
#             tubsonlar.append(n)
            
#     return tubsonlar
# print(tubtop(1, 50))


def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar


print(fibonacci(10))
