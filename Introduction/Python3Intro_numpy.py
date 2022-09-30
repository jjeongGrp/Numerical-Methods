# -*- coding: utf-8 -*-
#"""
#Created on Thu Sep 29 18:19:51 2022
#
#@author: jjeongGrp
#"""

# Creating an Array
from numpy import array
a = array([[-2.0, -1.9],[-1.0,3.0]])
print(a)

b = array([[2,-1],[-1,3]],float)
print(b)

from numpy import *
print(arange(2,10,2))
print(arange(2.0,10.0,2.0))

print(zeros(3))
print(ones((2,2)))


# Accessing and Changing Array Elements
from numpy import *
a = zeros((3,3),int)
print(a)
a[0] = [2,3,2]  # Change a row
print(a)
a[1,1] = 5      # Change an element
print(a)
a[2,0:2] = [8,-3] # Change part of a row
print(a)

# Operations on Arrays
from numpy import array
a = array([0.0, 4.0, 9.0, 16.0])
print(a/16.0)
print(a - 4.0)

from numpy import array, sqrt, sin
a = array([0.0, 4.0, 9.0, 16.0])
print(sqrt(a)/16.0)
print(sin(a))

# Array Functions

from numpy import *
A = array([[4,-2,1],[-2,4,-2],[1,-2,3]],float)
b = array([1,4,3],float)
print(diagonal(A)) # Principal diagonal
print(diagonal(A,1)) # First subdiagonal
print(trace(A)) # Sum of diagonal elements
print(argmax(b)) # Index of largest element
print(argmin(A,axis=0)) # Indices of smallest col. elements
print(identity(3)) # Identity matrix

from numpy import *
x = array([7,3])
y = array([2,1])
A = array([[1,2],[3,2]])
B = array([[1,1],[2,2]])

# Dot product
print("dot(x,y) = ",dot(x,y))  # {x}.{y}
print("dot(A,y) = ",dot(A,y))  # [A]{y}
print("dot(A,B) = \n",dot(A,B))  # [A][B], matrix product

# Inner product
print("inner(x,y) = ",inner(x,y))  # {x}.{y}
print("inner(A,y) = ",inner(A,y))  # [A]{y}
print("inner(A,B) = \n",inner(A,B))  # [A][B]', matrix product

# Outer product
print("outer(x,y) = \n",outer(x,y))  # {x}x{y}
print("outer(A,y) = \n",outer(A,y))  # [A]x{y}
print("outer(A,B) = \n",outer(A,B))  # [A]x[B]', dyadic product

# Linear algebra modulue
from numpy import array
from numpy.linalg import inv, solve
A = array([[4.0, -2.0, 1.0], \
           [-2.0, 4.0, -2.0], \
           [1.0, -2.0, 3.0]])
b = array([1.0, 4.0, 2.0])    
print(inv(A)) # Matrix inverse
print(solve(A,b)) # Solve [A]{x} = {b}


# Vectorizing Algorithms
from numpy import sqrt, sin, arange
from math import pi
x = arange(0.0, 1.001*pi, 0.01*pi)
print(sum(sqrt(x)*sin(x)))


