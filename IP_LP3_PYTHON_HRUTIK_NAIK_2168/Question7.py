# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:16:52 2020

@author: HRUTIK
"""

temp = input("Input the temperature you like to convert?(e.g,37C or 99F):")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")
