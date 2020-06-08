# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:17:08 2020

@author: HRUTIK
"""

def removeDuplicate(str): 

    

    t="" 

    for i in str: 

        if(i in t): 

            pass

        else: 

            t=t+i 

    print("",t) 

      

str=input("Enter text:")

removeDuplicate(str)