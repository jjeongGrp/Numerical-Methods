# -*- coding: utf-8 -*-
#"""
#Created on Sat Oct  1 18:35:36 2022
#
#@author: jjeongGrp
#"""

import numpy as np
from gaussElimin import *

# Vandermode matrices tend to be ill-conditioned
# A_{ij} = v^{n-j}_{i}, i=1,2,...,n,  j=1,2,...,n
def vandermode(v):
    n = len(v)
    A = np.zeros((n,n))
    for j in range(n):
        A[:,j] = v**(n-j-1)
    return A

v = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
b = np.array([0.0, 1.0, 0.0, 1.0, 0.0, 1.0])
A = vandermode(v)
Aorig = A.copy()  # Save original matrix
borig = b.copy()  # and the constant vector
x = gaussElimin(A, b)
det = np.prod(np.diagonal(A))

print('x = ', x)  # response
print('\ndet = ', det)
print('\nCheck result: [A]x - b =',np.dot(Aorig,x) - borig)
input('Press return to exit')

