'''Firs you need to install PyWebIO'''

## for installing use: pip install pywebio


from pywebio.input import input, FLOAT
from pywebio.output import put_text
from math import pi

def circle():
    r = input("Type radius of circle: ", type=FLOAT)
    s = pi*(r**2)
    p = 2*pi*r
    put_text(f"Square of circle equal to {s} and perimeter is equal to {p}")

circle()