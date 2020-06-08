# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:54:33 2020

@author: HRUTIK
"""

import datetime
a = int(input("Enter year:")) 
b = int(input("Enter month:"))
c = int(input("Enter Date:"))     
print("Week Number:",datetime.date(a, b, c).isocalendar()[1])