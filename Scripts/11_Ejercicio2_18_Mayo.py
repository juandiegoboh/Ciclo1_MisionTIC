# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:35:33 2021

@author: Juan Diego Bohórquez
"""
# Palindromo 

# Solución sin for
frase = input("Ingrese una frase palindroma: ").lower()
frase = frase.replace(" ","")
rever = frase[::-1]

print("La frase es palidroma" if frase == rever else "La frase no es palindroma")

# Solución con for

frase = input("Ingrese una frase palindroma: ").lower()
frase2 = frase.replace(" ","")

is_valid = True
max_index = len(frase2)-1
num_elements = len(frase2)

for i in range(0,num_elements):
    if frase2[i] != frase2[max_index]:
        is_valid = False
        break
    max_index -= 1

print(f"La frase {frase} es un palíndromo" if is_valid == True else f"La Frase {frase} no es un palíndromo")
      
# Solución 2 con for  
        
frase = input("Ingrese una frase palindroma: ").lower()
frase2 = frase.replace(" ","")

num_elements = len(frase2)

original = []
new_phrase = []

for letter in frase2:
    original.append(letter)
    
for index in reversed(range(0,num_elements)):
    letter = frase2[index]
    new_phrase.append(letter)

print(f"La frase {frase} es palindroma" if original == new_phrase else f"La frase {frase} no es palíndroma")

