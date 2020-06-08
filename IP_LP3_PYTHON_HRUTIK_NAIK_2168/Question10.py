# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:41:03 2020

@author: HRUTIK
"""

def selectionSort(nlist):
   for fillslot in range(len(nlist)-1,0,-1):
       maxpos=0
       for location in range(1,fillslot+1):
           if nlist[location]>nlist[maxpos]:
               maxpos = location

       temp = nlist[fillslot]
       nlist[fillslot] = nlist[maxpos]
       nlist[maxpos] = temp

nlist = []
n=int(input("Enter the number of elements to be sorted:"))
for i in range(0,n):
    ele = int(input("Enter the numbers:"))
    nlist.append(ele)
selectionSort(nlist)
print(nlist)