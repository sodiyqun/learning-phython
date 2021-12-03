# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 21:57:12 2021

@author: sodiyqun
"""

def info_yeg(name, surname, year, location, email='', phone=''):
    info = {
        'ism': name,
        'familiya': surname,
        'tyil': year,
        'yosh': 2021-year,
        'shahar': location,
        'e-pochta': email,
        'raqam': phone
        }
    return info

def info_kirit():   
    print("Userlarni qo'shamiz.")
    users = []
    while True:
        print("\nMa'lumotlarni kiriting", end='')
        ismi = input("Ismi: ")
        familiyasi = input("Familiyasi: ")
        tyili = int(input("Tug'ilgan yili: "))
        shahri = input("Tug'ilgan shahri: ")
        pochatasi = input("Elektron pochtasi: ")
        raqami = input("Telefon raqami: ")
        users.append(info_yeg(ismi, familiyasi, tyili, shahri, pochatasi, raqami))
        valid = input("Yana qo'shasizmi? (Ha/Yo'q)\n>>> ").lower()
        if valid == "yo'q" or valid == "y":
            break
    return users

def info_chiqar(users): 
    for user in users:
        if user['raqam']:
            number = user['raqam']
        else:
            number = "kiritilmagan"
        print(f"{user['ism'].title()} {user['familiya'].title()}, {user['yosh']} yoshda, telefon raqami: {number}.")





# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar


# print(fibonacci(10))
