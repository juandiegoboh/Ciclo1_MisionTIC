# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 21:33:09 2021

@author: Juan Diego Bohórquez
"""

def foo():
    print("", end="")

result = foo()

print(result)   # Retorna None así no se haya hecho ningún return

def foo():
    pass # Palabra clave analoga al continue en un loop

def foo():
    print("", end="")
    return("Hello", "world")

result = foo()

print(type(result))

var_1, var_2 = foo()

"""
Recursividad
"""

# Numeros factoriales: 3! = 1*2*3
# 4! = 1*2*3*4
# 0! = 1
# 1! = 1

def factorial(n):
    if n in [0, 1]:
        return 1
    
    result = n
    for k in range(2, n):
        result *= k
    
    return result

factorial(5)

# Función recursiva (se llama a si misma)

def factorial(n):
    if n in [0, 1]:
        return 1
    
    return factorial(n-1) * n

factorial(5)
