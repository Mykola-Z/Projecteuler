# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:19:35 2019

@author: mzly903
"""

import time 
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
print ('choose file:')
name = askopenfilename() # show an "Open" dialog box and return the path to the selected file
start = time.time()
data = np.loadtxt(name, delimiter=',')


def compute():
	ans = -1
	width = len(data[0])
	height = len(data)
	for y in range(height):
		for x in range(width):
			if x + CONSECUTIVE <= width:
				ans = max(grid_product(x, y,  1, 0, CONSECUTIVE), ans)
			if y + CONSECUTIVE <= height:
				ans = max(grid_product(x, y,  0, 1, CONSECUTIVE), ans)
			if x + CONSECUTIVE <= width and y + CONSECUTIVE <= height:
				ans = max(grid_product(x, y,  1, 1, CONSECUTIVE), ans)
			if x - CONSECUTIVE >= -1    and y + CONSECUTIVE <= height:
				ans = max(grid_product(x, y, -1, 1, CONSECUTIVE), ans)
	return str(ans)


def grid_product(ox, oy, dx, dy, n):
	result = 1
	for i in range(n):
		result *= data[oy + i * dy][ox + i * dx]
	return result

CONSECUTIVE = 4

if __name__ == "__main__":
	print(compute())

end = time.time()
spent = end - start
print ('calculation time is ' + str (spent) + ' s')