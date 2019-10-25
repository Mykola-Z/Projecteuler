# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:20:19 2019

@author: mzly903
"""
import time 
import math
start = time.time_ns()
def isprime(a):
    r=math.ceil(math.sqrt(a))
    list1=[]
    for i in range(3,r):
        if a%i==0:
            if isprime(i)==[]:
                list1.append(i)
    return list1
r=isprime(600851475143)
print(max(r))
end = time.time_ns()

print ('calculation time is ' + str(end-start) + ' ns')