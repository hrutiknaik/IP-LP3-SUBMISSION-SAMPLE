# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:03:07 2020

@author: HRUTIK
"""

def ngcd(x, y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i == 0):
            gcd=i;
        i+=1
    return gcd;
def num_comm_div(x, y):
  if (x>0 and x<(10**12+1) and y>=1 and y<(10**12+1)):
   n = ngcd(x, y)
   result = 0
   z = int(n**0.5)
   i = 1
   while( i <= z ):
     if(n % i == 0):
       result += 2 
       if(i == n/i):
         result-=1
     i+=1
   return result

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("Number of common divisors: ",num_comm_div(a, b))