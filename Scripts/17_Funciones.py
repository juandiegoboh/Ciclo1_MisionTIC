# -*- coding: utf-8 -*-
"""
Created on Tue May 25 20:10:48 2021

@author: Juan Diego Bohórquez
"""

# def squares(n):
#     for i in range(1,n+1):
#         if i != n:
#             print(i**2, end=", ")
#         else:
#             print(i**2)

# numero = int(input("Ingrese un número: "))

# squares(numero)

def squares(n):
    result = []
    for i in range(1,n+1):
        result.append(i**2)
    return result


numero = int(input("Ingrese un número: "))

resultado = squares(numero)

print(resultado)

for element in resultado:
    print(element, end= ", ")
    