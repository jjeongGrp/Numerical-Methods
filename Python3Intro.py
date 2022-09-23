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




