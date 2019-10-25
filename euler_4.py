# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:14:27 2019

@author: mzly903
"""

for i in range (100, 1000):
    for j in range (100, 1000):
        b = str (j*i)
        inverse = b [::-1]
        if inverse == b:
            palindromes.append(j*i)
g = max (palindromes)
print ('List of palindromes: ' )
print (palindromes)
print ('The highest palindrome is ' + str(g))
    
    