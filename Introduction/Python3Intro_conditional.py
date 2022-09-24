#"""
#Created on Sat Sep 24 11:54:28 2022
#
#@author: jjeongGrp
#"""

# Conditionals
def sign_of_a(a):
    if a < 0.0:
        sign = 'negative'
    elif a > 0.0:
        sign = 'positive'
    else:
        sign = 'zero'
    return sign
    
a4 = 2.0
print('a is' + ' ' + sign_of_a(a4))