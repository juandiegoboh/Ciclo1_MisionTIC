# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:22:59 2021

@author: Juan Diego Bohórquez
"""

n = int(input("Ingrese un número: "))

while not n in range (1,21):
    print("Error, vuelva a ingresar número")
    numero = int(input("Ingrese un número: "))

for i in range(1,n+1):
    print(f"El cubo de {i} es {i**3}")
    i += 1

# Solución 2
n = int(input("Ingrese un número: "))

i = 1
while n >= i:
    print(f"El cubo de {i} es {i**3}")
    i += 1

# Solución 3
n = int(input("Ingrese un número: "))

while n >= 1:
    print(f"El cubo de {n} es {n**3}")
    n -= 1

# Solución 4

n = int(input("Ingrese un número: "))

lista = []

while n >= 1:
    lista.append(n**3)
    n -= 1

lista.reverse()

for i in lista:
    print(i)