# -*- coding: utf-8 -*-
"""
Created on Wed May 26 20:49:40 2021

@author: Juan Diego Bohórquez
"""

lista = [True, "jose", "garcia", 1, 3.4, False, (), [], {"a": 1}]

def convertidor_lista(lista):
    for index, element in enumerate(lista):
    
        if type(element) in (int, float):
            lista[index] = element*2
            # lista[index] *= 2
                   
    return lista

resultado = convertidor_lista(lista)

print(resultado)

        