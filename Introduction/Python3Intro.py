#"""
#Created on Tue Jul  5 2022
#
#@author: jjeongGrp
#"""

# 1.2 Core Python
# Variables
b = 2      # b is integer type
print(b)
b = b*2.0  # Now b is float type
print(b)

# Strings
string1 = 'Press return to exit'
string2 = 'the program'
print(string1 +' '+ string2) # Concatenation with the plus (+)
print(string1[0:12])         # slicing (:)

s = '3 9 81' # string splited into component parts using the split command
print(s.split())  # Delimiter is white space

##string1[0] = 'p'  # string is an immutable object. TypeError happens

# Tuples
# Tuple is a sequence of arbitrary objects separted by commas and enclosed
# in parentheses.

rec = ('Karl','Franz',(10,11,2470))  # This is a tuple
print(rec)
firstName,lastName,birthdate = rec # Unpacking the tuple
print(firstName)
birthYear = birthdate[2]
print(birthYear)
name = rec[0] + ' ' + rec[1]
print(name)
print(rec[0:2])

# Lists

a = [1.0, 2.0, 3.0]  # Creat a list
a.append(4.0)      # Append 4.0 to list
print(a)

a.insert(0, -1.0)   # Insert 0.0 in position 0
print(a)
print(len(a))
a[2:4] = [-2.0, -3.0, -5.0] # Modify selected elements
print(a)

a1 = [1., 2., 3.]
b1 = a1             # b1 is an alias of a1
b1[0]=5.            # change b1
print(a1)           # The change is reflected in a1
print(a1[0])

c1 = a1[:]          # c1 is an independent copy of a1
c1[0] = -1.         # change c1
print(c1)           
print(a1)           # a1 is not affected by the change

a2 = [[1, 2, 3],\
      [4, 5, 6],\
          [7, 8, 9]]
print(a2[1])        # Print second row (element 1)
print(a2[1][2])     # Print third element of second row   


# Arithmetic Operators
# addition, subraction, multiplication, 
# division, exponentiation, modular division
# a += b,  a = a + b    addition
# a -= b,  a = a - b    subraction
# a *= b,  a = a * b    multiplication
# a /= b,  a = a / b    division
# a **= b, a = a ** b   exponentiation
# a %= b, a = a % b     modular division

s = 'Hello'
t = 'to you'
a3 = [1, 2, 3]
print(3*s)      # Repetition
print(3*a3)      # Repetition
print(a3 + [4,5]) # Append elements
print(s + ' ' + t)     # Concatenation
print(3 + s)      # This addition returns unspported operant types


# Comparision Operators

a3 = 2      # Integer
b2 = 1.999  # Floating point
c2 = '2'    # String
print(a3 > b2)  
print(a3 == c2)
print((a3 > b2) and (a3 != c2))
print((a3 > b2) or (a3 == b2))


# Type conversion
a = 5
b = -3.6
d = '4.0'
print(a + b)         # 1.4
print(int(b))        # -3.6 -> -3
print(complex(a,b))  # (5-3.6j)
print(float(d))      # 4.0
# print(int(d))     # ValueError: invalid literal for int() with base 10: '4.0'


# Reading Input

a = input('Input a: ')
print(a,type(a))
b = eval(a)
print(b,type(b))

# type 10.0
#Input a: 10.0
#10.0 <class 'str'>
#10.0 <class 'float'>

# type 11**2
#Input a: 11**2
#11**2 <class 'str'>
#121 <class 'int'>

a = eval(input('Input a:'))
print(a,type(a))

# type 3
#Input a:3
#3 <class 'int'>



# Printing Output
a = 1234.56789
b = [2, 4, 6, 8]
print(a,b) # 1234.56789 [2, 4, 6, 8]
print('a = ',a, '\nb =',b) 
# a =  1234.56789 
# b = [2, 4, 6, 8]


a = 1234.56789
n = 5876
print('{:7.2f}'.format(a))
print('n = {:6d}'.format(n))  # Pad with spaces
print('n = {:06d}'.format(n))  # Pad with zeros
print('{:12.3e} {:6d}'.format(a,n) )


# Writing Data to a File
f = open('testopen','w')
for k in range(101,111):
    f.write('{:4d} {:6d}'.format(k,k**2))
    f.write('\n')
f.close()
    
# Error control
try:
    c = 12.0/0.0
except ZeroDivisionError:
    print('Division by zero')

