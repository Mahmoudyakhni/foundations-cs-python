# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:44:46 2023

@author: mahmoud
"""

number_grade = eval(input("Enter your grade: "))
letter_grade = ""
if(number_grade >= 90):
    if(number_grade >= 97):
        print(number_grade,"is equivalent to a A+")
    elif(number_grade >= 94):
        print(number_grade,"is equivalent to a A")
    else:
        print(number_grade,"is equivalent to a A-")
elif(number_grade >= 80):
    if(number_grade >= 87):
        print(number_grade,"is equivalent to a B+")
    elif(number_grade >= 84):
        print(number_grade,"is equivalent to a B")
    else:
        print(number_grade,"is equivalent to a B")
elif(number_grade >= 70):
    if(number_grade >= 77):
        print(number_grade,"is equivalent to a C+")
    elif(number_grade >= 74):
        print(number_grade,"is equivalent to a C")
    else:
        print(number_grade,"is equivalent to a C-")
elif(number_grade >= 60):
    if(number_grade >= 67):
        print(number_grade,"is equivalent to a D+")
    elif(number_grade >= 64):
        print(number_grade,"is equivalent to a D")
    else:
        print(number_grade,"is equivalent to a D-")
else:
    if(number_grade >= 0):
        if(number_grade >= 30):
            print(number_grade,"is equivalent to a F1")
        elif(number_grade >= 10):
            print(number_grade,"is equivalent to a F2")
        else:
            print(number_grade,"is equivalent to a FF")