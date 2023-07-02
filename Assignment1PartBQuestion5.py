# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:45:03 2023

@author: mahmoud
"""
n = int(input("Enter a number: "))
for i in range(n + 1):
    for j in range(i):
        print("*",end = "")
    print("")
for k in range(n):
    for l in range(n-1,k,-1):
        print("*",end = "")
    print("")   
