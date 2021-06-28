# -*- coding: utf-8 -*-
"""
Created on Tue May 11 22:02:29 2021

@author: Juan Diego Bohórquez
"""

# Reto hackerrank

n = int(input("Enter an int number: "))
a, b = "Weird", "Not weird"

if n in range (1,101):    #Between 1 and 100
    if n%2 != 0:
        print(a)
    elif (n%2 == 0):
        if n in range(2,6): #Between 2 and 5
            print(b)
        elif n in range(6,21):  #Between 6 and 20
            print(a)
        else:
            print(b)
else:
    print("Number out of range")

