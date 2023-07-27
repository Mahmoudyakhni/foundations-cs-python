# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:45:24 2023

@author: mahmoud
"""
a = eval(input("Enter first number: ")) 
b = eval(input("Enter second number: "))
while(b < a):
    b = eval(input("Enter second number greater than first number: "))

if(a % 2 == 0):
    while(a<b):
        
        a+=2
        print(a, end=", ")
else:
    while(a<b):
        x=a+1
        a+=2
        print(x, end=", ")
    

    

