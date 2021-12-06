# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 00:10:56 2021

@author: sodiyqun
"""

# func10 = lambda x: x*10
# res = func10(20)

# print(res)


# funcsum_xy = lambda x, y: x + y
# res2 = funcsum_xy(10, 50)

# print(res2)


# from random import sample

# sonlar = sample(range(1001), 10)
# kv = list(map(lambda son: son**2, sonlar))
# toqs = list(filter(lambda son: son%2, sonlar))

# def tub(x):
#     if x%2 == 0 or x < 2:
#         return False
#     if x == 2 or x == 3:
#         return True
#     for n in range(3, x, 2):
#         if x%n == 0:
#             return False
#     return True

# tubsonlar = list(filter(tub, range(10001)))
# print(tubsonlar)