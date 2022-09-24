#"""
#Created on Sat Sep 24 11:59:47 2022
#
#@author: jjeongGrp
#"""

# Loops
# While loops
nMax = 5
n = 1
a = []               # Create empty list
while n < nMax:
    a.append(1.0/n)  # Append element to list
    n = n + 1
    
print(a) # [1.0, 0.5, 0.3333333333333333, 0.25]

# For loops
nMax = 5
a = []
print(a) # []
for n in range(1,nMax):
    a.append(1.0/n)
    
print(a) # [1.0, 0.5, 0.3333333333333333, 0.25]


# Break
list = ['JAck','Jill','Tim','Dave']
name = eval(input('Type a name: ')) # Python input prompt
for i in range(len(list)):
    if list[i] == name:
        print(name, ' is number', i + 1,' on the list')
        break
else:
        print(name,' is not on the list')
        
# Type 'Tim'
# Type 'June'


# Continue

x = []                     # Create an empty list
for i in range(1,100):
    if i%7 != 0: continue  # If not divisible by 7, skip rest of loop
    x.append(i)         # append i to the list
       
print(x)       # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]

