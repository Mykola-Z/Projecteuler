# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:19:35 2019

@author: mzly903
"""

import time 
import math
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
print ('choose file:')
name = askopenfilename() # show an "Open" dialog box and return the path to the selected file



#File uploading 
data = np.loadtxt(name) # OCT data
start = time.time()
list1 = []
for i in range(100):
    number=float(data[i])
    list1.append(number)
    
a = sum(list1)
string = str(a)
print (string[:11])    
        

end = time.time()
print ('calculation time is ' + str (end - start) + ' s')