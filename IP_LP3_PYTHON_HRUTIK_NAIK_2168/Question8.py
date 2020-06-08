# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:21:34 2020

@author: HRUTIK
"""

def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)
N=int(input("Enter the number:"))
sum_series(N)