# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:41:54 2023

@author: mahmoud
"""

id = input("Enter user's ID: ")
name = input("Enter user's name: ")
date_of_birth = input("Enter user's birthday in the following format DD/MM/YYY: ")
address = input("Enter user's address: ")

print("Your profile - ID:0"+id+", name:"+name.upper()+", DOB:"+date_of_birth+",Address:"+address.lower().strip())
