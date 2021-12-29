# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:28:05 2021

@author: sodiyqun
"""

def kattasini_top(x, y ,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    elif x == y and x > z:
        return x
    elif z == x and x > y:
        return z
    elif y == z and y > x:
        return y
    else:
        return x