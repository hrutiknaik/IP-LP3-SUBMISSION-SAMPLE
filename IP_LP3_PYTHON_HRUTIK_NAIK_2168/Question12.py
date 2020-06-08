# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:57:58 2020

@author: HRUTIK
"""

from collections import Counter
classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VI', 4),
    ('VII', 1),
    ('X', 1),
)
students = Counter(class_name for class_name, no_students in classes)
print(students)