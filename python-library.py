# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 05:09:15 2021

@author: sodiyqun
"""

import datetime as dt
import re

b = dt.date.today()
# delta = dt.timedelta(weeks=1)

# for x in range(10):
#     b += delta
#     print(b)
    
# print('')

# q = dt.date.today() + dt.timedelta(weeks=10)
# a = dt.date.today()
# while a != q:
#     a += dt.timedelta(weeks=1)
#     print(a)


# ramadan = dt.date(2022, 4, 2)
# farq1 = ramadan - b

# aid = dt.date(2022, 7, 9)
# farq2 = aid - b
# print(f"Ramazongacha {farq1.days} kun qoldi, \nQurbon hayitgacha {farq2.days} kun qoldi.")


# birth = dt.date(2004, 1, 22)
# farq = b - birth
# days = farq.days
# months = int(days/30)
# years = int(months/12)
# print(f"{years} yil\n{months} oy\n{days} kun")


# approved = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
# phone = input("Telefon raqam kiriting: ")
# while True:
#     # phone = int(input("Telefon raqam kiriting: "))
#     if re.match(approved, phone):
#         print("Qabul qilindi")
#         break
#     else:
#         phone = input("Iltimos to'g'ri kiriting\n>>>")










## FAIL

# approved = 'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'

# matn = """Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI \nUshbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

# sample = """yuklandi: https://youtu.be/vsxJPRLXpgI"""
# u = re.findall(approved, s)
# print(u)