# -*- coding: utf-8 -*-
#"""
#Created on Thu Sep 29 21:58:19 2022
#
#@author: jjeongGrp
#"""

import matplotlib.pyplot as plt
from numpy import arange, sin, cos
x = arange(0.0, 6.2, 0.2)

plt.plot(x,sin(x),'o-',x,cos(x),'>-') # Plot with specified line and marker style
plt.xlabel('x')                       # Add label to x-axis
plt.legend(('sine','cosine'),loc=0) # Add legend in loc. 3
plt.grid(True)  # Add coordinate grid
plt.savefig('testplot.png',format='png') # save plot in png format for future use
plt.show()
input("Press return to exit")


plt.subplot(2,1,1)
plt.plot(x,sin(x),'o-')
plt.xlabel('x');plt.ylabel('sin(x)')
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(x,cos(x),'^-')
plt.xlabel('x'); plt.ylabel('cos(x)')
plt.grid(True)
plt.show()
input("\nPress return to exit")