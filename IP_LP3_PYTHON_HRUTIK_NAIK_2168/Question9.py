# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:33:00 2020

@author: HRUTIK
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_BST(root):
    stack = []
    prev = None
    
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and root.val <= prev.val:
            return False
        prev = root
        root = root.right
    return True
a = int(input("Enter root node:")) 
root = TreeNode(a)  
b= int(input("Enter left node:")) 
root.left = TreeNode(b)
c = int(input("Enter right node:"))   
root.right = TreeNode(c) 
 
result = is_BST(root)
print(result)

