# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:26:29 2020

@author: HRUTIK
"""

year = int(input("Please Enter the Year Number you wish: "))

if 1900<=year<=10:
    if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
        print("TRUE")
    else:
        print("FALSE")
else:
    print("FALSE")