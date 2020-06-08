# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:04:39 2020

@author: HRUTIK
"""

a = int(input())                          #Read two integers
b = int(input())

if 1<=a<=10**10 and 1<=b<=10**10:         #constraints
 sum = a+b
 difference = a-b
 product = a*b

 print (sum)                              #The first line contains the sum of the two numbers.
 print (difference)                       #The second line contains the difference of the two numbers (first - second).
 print (product)                          #The third line contains the product of the two numbers.