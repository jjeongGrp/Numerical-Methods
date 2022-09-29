# -*- coding: utf-8 -*-
#"""
#Created on Thu Sep 29 17:54:11 2022
#
#@author: jjeongGrp
#"""

# Functions
def derivatives(f,x,h=0.0001):
    df = (f(x+h) - f(x-h)) / (2.0*h)
    ddf = (f(x+h) -2.0*f(x) + f(x-h)) / h**2
    return df,ddf

from math import atan
df,ddf = derivatives(atan,0.5) 
print('First derivative =', df)
print('Second derivative =', ddf)

def squares(a):
    for i in range(len(a)):
        a[i] = a[i]**2
        
a = [1,2,3,4]        
squares(a)
print(a)  # a now contains a**2


# Lambda statement
c = lambda x,y : x**2 + y**2
print(c(3,4))

# Math module
from math import log,sin
print(log(sin(0.5)))

import math
print(math.log(math.sin(0.5)))

import math as m
print(m.log(m.sin(0.5)))

import math
dir(math)

# cmath module, complex functions

from cmath import sin
x = 3.0 - 4.5j
y = 1.2 + 0.8j
z = 0.8
print(x/y)
print(sin(x))
print(sin(z))
