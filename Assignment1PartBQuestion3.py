# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:44:24 2023

@author: mahmoud
"""

number = input("Enter a number to show how much digits contains: ")
s =  number
x=0
for i in range(len(s)):
    if(s[i]==0 or s[i]==1):
     x+=1
print(s,"has",x,"digits")