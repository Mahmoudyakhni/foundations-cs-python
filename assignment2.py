# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 15:59:34 2023

@author: mahmoud
"""
#############################################
##  Assignment 2  ###########################
#############################################

###########################################
##  Question 1  ###########################
###########################################

def reverseConcWord(word, n):
    word = word[::-1]
    return word * n  
n = 3
word = "hello"
reversed_concatenated_word = reverseConcWord(word, n)
print(reversed_concatenated_word)


###########################################
##  Question 2  ###########################
###########################################

def capitalLettersToLeft(word):
    lower = ""
    upper = ""    
    for char in word:
        if char.isupper():
            upper += char
        else:
            lower += char    
    return upper + lower
word = "Hello World"
print(capitalLettersToLeft(word))

###########################################
##  Question 3  ###########################
###########################################

def compareTwoWords(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    if(s1 == s2):
        return True
    else:
        return False
s1 = "abcde"
s2 = "edacb"
x = compareTwoWords(s1, s2)
print(x) 

###########################################
##  Question 4  ###########################
###########################################

def maxValueIndex(l):
    max_value = l[0]
    max_index = 0
    for i in range(1, len(l)):
        if l[i] >= max_value:
            max_value = l[i]
            max_index = i
    return  max_value, max_index
list1 = [5, 6, 3, 2, 7, 2, 0, 1, 6]
max1, index1 = maxValueIndex(list1)
print("the highest value in the list is", max1, "at index", index1)


def minValueIndex(l):
    min_value = l[0]
    min_index = 0
    for i in range(1, len(l)):
        if l[i] <= min_value:
            min_value = l[i]
            min_index = i
    return  min_value, min_index
list1 = [5, 6, 3, 2, 7, 2, 0, 1, 6]
min1, index1 = minValueIndex(list1)
print("the lowest value in the list is", min1, "at index", index1)     

###########################################
##  Question 5  ###########################
########################################### 

def sumDigitNumber(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        while(n != 0):
            sum = n % 10
            n = n//10
            return sum + sumDigitNumber(n)        
n = 12345
result = sumDigitNumber(n)
print(result)

###########################################
##  Question 6  ###########################
###########################################  

def removeDuplicateChar(s):
    if len(s) < 2:
        return s
    if (s[0] in s[1:]):
        return removeDuplicateChar(s[1:])
    else:
        return s[0] + removeDuplicateChar(s[1:])
s = "hhheeeelllllooooo wwwwooooorrrrllllldddd"
s_removed_dublicate = removeDuplicateChar(s)
print(s_removed_dublicate)
    
###########################################
##  Question 7  ###########################
###########################################
 
def reverse_number(n):
    if n < 10:
        return n
    else:
        reminder = n % 10
        number_wout_last_nb = n // 10
        x = len(str(number_wout_last_nb))
        return reminder * 10 ** x + reverse_number(number_wout_last_nb)
reversed_number = reverse_number(2366497461649464)
print(reversed_number)

#################################### DONE #####################################

        
            


    