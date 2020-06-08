# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:43:17 2020

@author: HRUTIK
"""

import math
import os
import random
import re
import sys
    
def countSpecialElements(a):
  nRows= len(a)
  nCount=0
  
  for row in a:
    for indexCol, element in enumerate(row):
  
      if element==min(row) or element==max(row):
        if row.count(element)>1:
          return -1
        nCount=nCount+1
  
      else:
        listColumn=[]
  
        for indexRow in range(0, nRows):
          listColumn.append(a[indexRow][indexCol])
  
        if element==min(listColumn) or element==max(listColumn):
          if listColumn.count(element)>1:
            return -1
          nCount=nCount+1
 
  return nCount
  
if __name__ == '__main__':
    R = int(input("Enter the number of rows:")) 
    C = int(input("Enter the number of columns:"))  
    matrix = [] 
    print("Enter the entries rowwise:") 
  
    for i in range(R):          
     a =[] 
     for j in range(C):       
         a.append(int(input())) 
     matrix.append(a)
    nCount = countSpecialElements(matrix)
    print("Special Element:",nCount)