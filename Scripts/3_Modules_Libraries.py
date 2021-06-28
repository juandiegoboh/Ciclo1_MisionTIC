# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:26:23 2021

@author: Juan Diego Bohórquez
"""

import math

my_number = 3.4
print(math.floor(my_number))
print(math.sqrt(my_number))
print(math.pi, math.e)

#Create a program that calculates the hypotenuse of a rect angle triangle

print("This program will show the hypotenuse of a right triangle")
c1,c2 = input("Insert the two legs of the triangle with a space between: ").split()
c1,c2 = float(c1),float(c2)
h = math.sqrt((c1**2) + (c2**2))

print("The hypotenuse is: {}".format(h))

#Create a program that calculaes the area of a circle using a radius given by the user

print("This program will show the area of a circle given its radius")
r = float(input("Insert the radius: "))
area = math.pi*(r**2)

print("The area of your circle is: {:.2f}".format(area))

#Exercise

bool_1 = int(True)
bool_2 = int(False)

num = float(input("Please insert a number: "))
result = math.floor(numero**3)
print("The nearest smallest integer of the cube is {:.2f}".format(result))
