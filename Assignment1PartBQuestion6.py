# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:45:24 2023

@author: mahmoud
"""
a = eval(input("Enter first number: ")) 
b = eval(input("Enter second number: "))
while(b < a):
    b = eval(input("Enter second number greater than first number: "))
c = a
if(a % 2 == 0):
    while(c<b):
        list1 = a + 2
        c+=2
        a+=2
        print(list1, end=", ")
else:
    while(c<b):
        list1 = a + 1
        c+=2
        a+=2
        print(list1, end=", ")
    
    
    

