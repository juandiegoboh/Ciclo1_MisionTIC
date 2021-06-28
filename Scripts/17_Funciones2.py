# -*- coding: utf-8 -*-
"""
Created on Tue May 25 20:39:46 2021

@author: Juan Diego Bohórquez
"""

"""
Write a Python program to reverse a string
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""

# Solución 1

frase = input("Ingrese una frase: ")

def reverse_string(frase):
    return frase[::-1]

resultado = reverse_string(frase)
print(resultado)

"""
Write a Python function to find the Max of three numbers.
"""

def numero_mayor(a,b,c):
    return f"El numero mayor es {max(a,b,c)}"

a, b, c = input("Ingrese 3 numeros separados: ").split()

resultado = numero_mayor(a,b,c)
print(resultado)

"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
[1, 2, 3, 4, 5, 4, 3, 7, 9]
[1, 2, 3, 4, 5, 7, 9]
"""

numeros = input("Ingrese un grupo de numeros: ").split()

def unicos(numeros):
    lista_unica = []
    for i in numeros:
        if i not in lista_unica:
            lista_unica.append(i)
    return lista_unica
            
resultado = unicos(numeros)            

print(resultado)

"""
Hackerrank

"""

# https://www.hackerrank.com/challenges/find-a-string/problem
long_str = input("Ingrese una frase larga:")
short_str = input("Ingrese una frase corta:")

def count_substring(long_str, short_str):
    counter = 0
    for l in range(0, len(long_str)):
        if short_str ==  long_str[l:l + len(short_str)]:
            counter += 1

    return counter

resultado = count_substring(long_str, short_str)
print(resultado)

"""
Tiene un bug si la cadena corta termina con la letra con la que empieza
"""

def comparar_cadena(CadenaLarga,CadenaCorta):
    while len(CadenaLarga)>200 or len(CadenaCorta)>len(CadenaLarga):
        CadenaLarga=input('ingrese cadena de texto para anlizar:\n')
        CadenaCorta=input('ingrese Cadena corta de texto: \n')
    letras1=len(CadenaLarga)
    letras2=len(CadenaCorta)
    letras3=len(CadenaLarga.replace(CadenaCorta,''))
    numero_repeticiones=int((letras1-letras3)/letras2)
    print(f'La cadena de texto "{CadenaCorta}" se repite {numero_repeticiones} veces en "{CadenaLarga}"')


Cadena1=input('ingrese cadena de texto para anlizar:\n')
Cadena2=input('ingrese Cadena corta de texto: \n')

comparar_cadena(Cadena1,Cadena2)
