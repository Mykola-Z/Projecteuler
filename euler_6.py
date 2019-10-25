# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:37:21 2019

@author: mzly903
"""

import time 
start = time.time_ns()

a = range (1, 101)

sum_sq_list = []
just_sum_list = []
for i in a:
    sum_sq = i**2
    just_sum = i
    sum_sq_list.append(sum_sq)
    just_sum_list.append(just_sum)
calculate1 = sum(sum_sq_list) 
calculate2 = sum(just_sum_list)**2

result = calculate2- calculate1

print ('result is ' + str(result))

end = time.time_ns()
spent = end - start
print ('calculation time is ' + str (spent) + ' ns')

