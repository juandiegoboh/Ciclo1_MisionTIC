# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 20:20:25 2021

@author: Juan Diego Bohórquez
"""

import glob

list_1 = glob.glob("./*")   # Hace una lista, se puede saber la longitud

list_2 = glob.iglob("./*")  # Hace un generador, ocupa mucho menos espacio al ser 1 solo elemento

for element in list_1:
    print(element)

print("****")

for element in list_1:
    print(element)
    
"""
Funciones anonimas
"""

# reference
# MLA, 8.ª edición (Modern Language Assoc.)
# Romano, Fabrizio, et al. Python: Journey From Novice to Expert. Packt Publishing, 2016.

# APA, 7.ª edición (American Psychological Assoc.)
# Romano, F., Phillips, D., & Hattem, R. van. (2016). Python: Journey From Novice to Expert. Packt Publishing.

#  example 1: adder
 
def adder(a, b):
    return a + b
    
# is equivalent to:

adder_lambda = lambda a, b: a + b

# example 2: to uppercase
def to_upper(s):
    return s.upper()

# is equivalent to:

to_upper_lambda = lambda s: s.upper()

# Ejemplo con lambda y map

nums = [-2, 3, 5, 3, 18, 29]

nums_sqr = [i**2 for i in nums]

def square(number):
    return number **2
    
map(square, nums)
list(map(square, nums))

list(map(lambda x: x**2, nums))

def is_multiple_5(number):
    return number % 5 == 0

filter(is_multiple_5, nums)
list(filter(is_multiple_5, nums))

list(filter(lambda x: x % 5 == 0, nums))

# Exercise: Transform to lambda type the below functions

def is_multiple_of_five(n):
    return not n % 5

def get_multiples_of_five(n):
    return list( filter(is_multiple_of_five, range(n)))

print(get_multiples_of_five(50))

#  Write a Python program to filter a list of integers using Lambda that returns the even numbers

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
pares = list(filter(lambda x: x % 2 ==0, nums))
print(pares)

cuadrados = list(map(lambda x: x**2, nums))
cubos = list(map(lambda x: x**3, nums))

print(cuadrados, cubos)



