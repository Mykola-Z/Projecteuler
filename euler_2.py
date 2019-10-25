# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 18:20:19 2019

@author: mzly903
"""
import time

start= time.time_ns()
set = [1,2]

while sum(set) < 4000000:
    b = set [-1] + set [-2]
    
    set.append(b)
end=time.time_ns() 

time = end - start

print(time)   
print (sum(set))