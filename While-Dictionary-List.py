# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 03:18:40 2021

@author: sodiyqun
"""

# savat = []
# savol = "Savatga mahsulot qo'shing: "
# while True:
#     mahsulot = input(savol).lower()
#     savat.append(mahsulot)
#     again = input(f"Yana mahsulot qo'shishni istaysizmi? (Ha/Yo'q)\n>>> ")
#     if again.lower() != 'ha':
#         break
    
# print("Savatdagi mahsulotlar:")
# for mahsulot in savat:
#     print(mahsulot.title() + ", ", end='')


# mahsulotlar = {}
# while True:
#     mahsulot = input("Mahsulot nomini kiriting: ").lower()
#     narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
#     mahsulotlar[mahsulot] = narh
#     again = input(f"Yana mahsulot qo'shishni istaysizmi? (Ha/Yo'q)\n>>> ")
#     if again.lower() != "ha" or again.lower() != "1":
#         break
    
# print("Mahsulotlar:")
# for mahsulot, narh in mahsulotlar.items():
#     print(f"{mahsulot.title()}ning narhi - {narh} so'm")


# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()}ning narhi - {narh} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")