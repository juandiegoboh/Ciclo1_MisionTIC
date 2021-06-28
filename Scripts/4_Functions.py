# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:27:37 2021

@author: Juan Diego Bohórquez
"""

def sum_two(number_a,number_b):
    result = number_a + number_b
    print(f"The sum of {number_a} and {number_b} is: {result}")

a = 1
b = 7
    
sum_two(a,b)

#Write a function that calculates the tangent of an angle given by the user
from math import tan

def tangent(angle):
    """
    Function that calculates the tangent using a given angle

    Parameters
    ----------
    angle : float

    Returns
    -------
    result : float
        Tangent calculated in radians.
    """
    result = tan(angle)
    return result

a1 = float(input("Please enter an angle: "))
calculo = tangent(a1)

print("The tangent calculated for {} is {:.2f}".format(a1,calculo))

"""
Operadores logicos
"""

input_1 = True
input_2 = False
input_3 = True

print(input_1 and input_2 and input_3)

input_1 = True
input_2 = False
input_3 = True

print(input_1 or input_2 or input_3)



