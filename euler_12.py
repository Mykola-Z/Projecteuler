# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:19:35 2019

@author: mzly903
"""

import time 
import math
import numpy as np

start = time.time()

limit = 501
x = 2 # 1 and number itself 
i=0
number = 0
while x <= limit:
    i+=1
    number = number + i 
    x=2
    for j in range (2, (math.ceil(math.sqrt(number)))):
        if number % j ==0:
            x+=2
    
print (number)
        

end = time.time()
print ('calculation time is ' + str (end - start) + ' s')