# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 16:03:05 2021

@author: sodiyqun
"""

# son = float(input('Juft son kiriting: '))
# if son%2:
#     print('Bu juft son emas!')
# else:
#     print('Rahmat!')


# yosh = int(input('Yoshingizni kiriting: '))
# if yosh <= 4 or yosh >= 60:
#     print('Sizga kirish bepul')
# elif yosh < 18:
#     print('Sizga kirish 10,000 so\'m')
# else:
#     print('Sizga kirish 20,000 so\'m')


# x = float(input('Birinchi soni kiriting: '))
# y = float(input('Ikkinchi soni kiriting: '))
# if x > y:
#     print(f'\n{x} > {y}')
# elif x < y:
#     print(f'\n{x} < {y}')
# else:
#     print(f'\n{x} = {y}')


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append((input(f'Savatga {n+1}chi mahsulotni qo\'shing: ')).lower())
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f'Do\'konimizda {mahsulot} bor')
#     else:
#         print(f'Do\'konimizda {mahsulot} yo\'q')


# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append((input(f'Savatga {n+1}chi mahsulotni qo\'shing: ')).lower())
# bor = []
# yoq = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor.append(mahsulot)
#     else:
#         yoq.append(mahsulot)
# if yoq:
#     print('\nDo\'konimizda quyidagi mahsulotlar yo\'q:')
#     for mahsulot in yoq:
#         print(mahsulot)
# else:
#     print('\nSiz so\'ragan barcha mahsulotlar do\'konimizda bor')


# users = ['alisher','aziza','yasina','umar']
# login = input('Yangi login kiriting: ')
# login = login.lower()
# if login in users:
#     print('Bu Login band, boshqa login tanlang')
# else:
#     print(f"Xush kelibsiz, {login.title()}!")


son = int(input('Istalgan son kiriting: '))
for n in range(2,11):
    if not (son%n):
        print(f'{son} soni {n}ga qoldiqsiz bo\'linadi')