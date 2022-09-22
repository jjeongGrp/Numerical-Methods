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



