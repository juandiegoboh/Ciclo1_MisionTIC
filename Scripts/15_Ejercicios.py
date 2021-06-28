# -*- coding: utf-8 -*-
"""
Created on Mon May 24 21:27:24 2021

@author: Juan Diego Bohórquez
"""

"""
Create a program that verifies if a parenthesis inside a phrase is properly closed
Crea un programa que verifique si un parentésis dentro de una frase es cerrado correctamente

print('hello')  --> True
Estaba en el mercado (aunque no queria) mientras mi hermano se quedó durmiendo --> True
Estaba en el mercado (aunque no queria mientras mi hermano se quedó durmiendo --> False
(hola carambola (estas cerrando) (muy mal los parentesis --> False
(hola carambola) (estas cerrando) (muy bien los parentesis) --> True
(hola carambola (estas cerrando (muy bien los parentesis))) --> True
"""

# Solucion super larga

frase = input("Ingrese una frase: ")

conteo = {}

for char in frase:
    if char == "(" or ")":
        if char not in conteo:
            conteo[char] = 1
    
        else:
            conteo[char] += 1

if list(conteo.values())[0] == list(conteo.values())[1]:
    print("Es correcto")

else:
    print("No es correcto")
    
# Solucion 2

contador = 0

for letter in frase:
    if letter == "(":
        contador += 1
    if letter == ")":
        contador -= 1

print("Es correcto" if contador == 0 else "Es incorrecto")
        
# Solucion 3
    
parentesis_abren = 0
parentesis_cierran = 0

for letter in frase:
    if letter == "(":
        parentesis_abren += 1
    elif letter == ")":
        parentesis_cierran += 1

print("Es correcto" if parentesis_abren == parentesis_cierran else "Es incorrecto")

"""
**************************************************
"""
# List comprehension

squares = [i**2 for i in range(1,11)] 

squares = [i**2 for i in range(1,11) if (i**2) % 2 == 0]
  