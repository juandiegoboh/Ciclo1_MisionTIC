# -*- coding: utf-8 -*-
"""
Created on Fri May 14 20:15:39 2021

@author: Juan Diego Bohórquez
"""

my_str = input("Ingrese un valor de la forma A,1,2: ")

lista = my_str.split(",")
cambio = lista.pop(0)

maximo = max(lista)
minimo = min(lista)

print("El valor máximo de la lista {} es {}. El valor mínimo es {}".format(cambio,maximo,minimo))

#
#
# Ejercicio codechef
#
#

l_muerto = input("Ingrese dos palabras de lenguaje muerto: ")
l_moderno = input("Ingrese una frase de 3 palabras: ")

lista_1 = l_muerto.split(" ")
lista_2 = l_moderno.split(" ")

if lista_1[0] in lista_2:
    print("{}: Yes".format(lista_1[0]))
else:
    print("{}: No".format(lista_1[0]))

if len(lista_1) > 1:
    
    if lista_1[1] in lista_2:
        print("{}: Yes".format(lista_1[1]))
    else:
        print("{}: No".format(lista_1[1]))


