# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:37:21 2019

@author: mzly903
"""

import time 
import math
import numpy
start = time.time_ns()


def isprime(x):
    limit = math.ceil(math.sqrt(x)) + 1
    for i in range(2, limit):
        if x % i == 0:
            return False
    return True

primes = [1, 2]
prime = 3
for i in range (3, 2000000):
    
    if isprime(i) is True:
        prime +=i


        
print ('The sum of all the primes below two million ' + str(prime))


end = time.time_ns()
spent = end - start
print ('calculation time is ' + str (spent) + ' ns')

