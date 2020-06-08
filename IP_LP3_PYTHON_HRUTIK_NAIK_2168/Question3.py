# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:03:45 2020

@author: HRUTIK
"""

N=int(input())
dict={}
li=[]
for i in range(N):
    word=input()
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
        li.append(word)
print (len(li))      
for i in li:
    print (dict[i])