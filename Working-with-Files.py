# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 20:50:48 2021

@author: sodiyqun
"""

import pickle

with open('logs/pi_million_digits.txt') as file:
    pi = file.read()
    
pi = pi.rstrip()
pi = pi.replace('\n', '')
pi = pi.replace(' ', '')

birthdate = '22012004'
if birthdate in pi:
    print("Bor")
else:
    print("Yo'q")

pi = float(pi)

with open('logs/pi_float.dat', 'wb') as file:
    pickle.dump(pi, file)


## Type below in console
# with open('logs/pi_float.dat', 'rb') as f:
#     i = pickle.load(f)
# print(i)



while True:
    movies = input("Yaxshi koʻrgan filmlaringizni kiriting (to'xtash uchun Enter bosing): ")
    if not movies: break
    with open('logs/movies.txt', 'a') as file:
        file.write(movies+'\n')
