# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 13:19:28 2021

@author: sodiyqun
"""

import random

def sontopme(x=10):
    tson = random.randint(1,x)
    print(f"Men 1dan {x}gacha son o'yladim. Topa olasizmi?", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>> "))
        if tson>taxmin:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:", end="")
        elif tson<taxmin:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:", end="")
        else:
            break
        
    print(f"\nTabriklayman. {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar


def sontoppc(x=10):
    input(f"1 dan {x} gacha son o'ylang va \"Enter\" tugmasini bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori: #fitc
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        # taxmin = random.randint(quyi,yuqori)
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)\n>>> ")
        if javob.lower() == "-":
            yuqori = taxmin - 1 
        elif javob.lower() == "+":
            quyi = taxmin + 1
        else:
            break
        
    print(f"\nMen {taxminlar} ta taxmin bilan topdim!")
    return taxminlar


def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontopme(x)
        taxminlar_pc = sontoppc(x)
        if taxminlar_user>taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0): "))
        
play()