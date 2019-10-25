# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:37:21 2019

@author: mzly903
"""

import time 
import numpy as np
start = time.time_ns()

sum = 1
b=1 
while sum !=1000:
    b +=1     
    for j in range(1,b):
        a = j
        c_2 = b**2+a**2
        c= np.sqrt(c_2)
        if c == round(c):
            sum = a + b + c
            if sum == 1000:
                print ('Here we go {} + {} + {} = 1000'.format(a, b, c))                
                break
    

end = time.time_ns()
spent = end - start
print ('calculation time is ' + str (spent) + ' ns')

