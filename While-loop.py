# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 01:56:05 2021

@author: sodiyqun
"""

# books = []
# q = "Yaxshi ko'rgan kitoblaringiz nomini kiriting "
# q += "(toxtatish uchun 'stop' deb yozing)"
# while True:
#     kitob = input(f"{q}\n>>> ")
#     if kitob == 'stop':
#         break
#     else:
#         books.append(kitob)
# print("Yaxshi ko'rgan kitoblaringiz:")
# for book in books:
#     print(book.title())


# savol = "Yoshingizni kiriting: "

# while True:
#     yosh = input(savol)
#     if yosh == 'exit' or yosh == 'quit':
#         break
#     yosh = int(yosh)
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 30000
#     elif 18<=yosh<65:
#         narh = 100000
#     else:
#         narh = 0
#     if narh == 0:
#         print("Sizga kirish bepul!")
#     else:
#         print(f"Sizga kirish {narh} so'm")
# print("Dastur yoxtatildi!")


# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# while True:
#     qiymat = input(savol)
#     if float(qiymat)<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")