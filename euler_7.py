# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:37:21 2019

@author: mzly903
"""

import time
import math
start = time.time_ns()


def isprime(x):
    limit = math.ceil(math.sqrt(x)) + 1
    for i in range(2, limit):
        if x % i == 0:
            return False
    return True

primes = [1, 2]
i = 2
number = 10001
while len(primes) < number:
    i += 1
    if isprime(i) is True:
        primes.append(i)
print ('{}th prime = {}'.format(number, primes[-1]))

end = time.time_ns()
spent = end - start
print ('calculation time is ' + str(spent) + ' ns')