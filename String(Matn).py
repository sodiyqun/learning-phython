# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 23:13:53 2021

@author: sodiyqun
"""

# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor" 
# viloyat = "Samarqand"
# print(kocha, "ko'chasi,", mahalla, "mahallasi,", tuman, "tumani,", viloyat, "viloyati.")


kocha = input("Ko'changizni nomini kiriting \n>>> ")
kocha = kocha.capitalize()
mahalla = input("Mahallangizni nomini kiriting \n>>> ")
mahalla = mahalla.capitalize()
tuman = input("Tumaningizni nomini kiriting \n>>> ")
tuman = tuman.capitalize()
viloyat = input("Viloyatingizni nomini kiriting \n>>> ")
viloyat = viloyat.capitalize()
print(kocha, "ko'chasi,", mahalla, "mahallasi,", tuman, "tumani,", viloyat, "viloyati.")

manzil = f'{kocha} ko\'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat}, viloyati.'
print(manzil)

# manzil = manzil.title()
# manzil = manzil.upper()
# manzil = manzil.lower()
# manzil = manzil.capitalize()

# print(manzil.title())
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.capitalize())
