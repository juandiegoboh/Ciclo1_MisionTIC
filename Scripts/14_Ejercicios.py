# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:17:24 2021

@author: Juan Diego Bohórquez
"""
letters = ["a", "b", "c", "d"]
frequency = [0, 3, 8, 5]

score = {}

# score["a"] = 1

# for letter, number in zip(letters, frequency):
#     score[letter] = number

# for key, value in score.items():
#     print(key, value)

"""
Dada una cadena de caracteres, determine cual es el caracter que mas se repite y
cuantas veces(case insensitive)
ejemplo: input = 'hola soy la letra mas repetida'
output = a 5
"""

frase = input("Ingrese una frase: ").lower()
frase = frase.replace(" ","")

repeticion = {}

for letra in frase:
    if letra in repeticion.keys():
        repeticion[letra] += 1 # Si la letra existe se le suma +1 a los values
    
    else:
        repeticion[letra] = 1   # Si la letra no existe toma el valor de 1 como valor inicial


for key, value in repeticion.items():
    if max(repeticion.values()) == 1:
        print(f"Todas las letras se repiten {value} vez.")
        break
    elif value == max(repeticion.values()):
        print(f"La letra '{key}' es la más repetida, se repite {value} veces.")


        

    
    