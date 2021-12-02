# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:06:50 2021

@author: sodiyqun
"""

# def kopaytir(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son 
#     return kopaytma

# print(kopaytir(4,5,6))


def tinfo(ism, familiya, **infos):
    infos['ismi'] = ism
    infos['familiyasi'] = familiya
    return infos

talaba = tinfo('olim', 'olimov', tyili = 1995, fakulteti ='IT', yonalishi = 'AT')