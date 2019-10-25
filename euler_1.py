# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:20:19 2019

@author: mzly903
"""
import time 
import math
start = time.time_ns()
def issimple(a):
    r=math.ceil(math.sqrt(a))
    lst=[]
    for i in range(3,r):
        if a%i==0:
            if issimple(i)==[]:
                lst.append(i)
    return lst
r=issimple(600851475143)
print(max(r))
end = time.time_ns()

print ('calculation time is ' + str(end-start) + '')