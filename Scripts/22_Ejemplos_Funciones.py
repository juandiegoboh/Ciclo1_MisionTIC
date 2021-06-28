# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 20:18:36 2021

@author: Juan Diego Bohórquez
"""

def foo(a,b,c=1,d=10):
    print(a,b,c,d)

foo(1,5)    

def print_data(name, surname, birthday = None):
    if birthday is None:
        print(name, surname)
    else:
        print(name, surname, birthday)

print_data("Juan Diego", "Bohórquez")
print_data("Juan Diego", "Bohórquez", birthday = "25/07/1997")

import datetime

def func(delta_days = 5):
    return datetime.datetime.now() + datetime.timedelta(days = delta_days)

resultado = func(9)

print(resultado)

import math

# Se puede apuntar una variable hacia una funcion, sin ejecutarla, es decir sin ().
# Esta solución es una opción cuando se necesita usar muchas funciones de un modulo, 60 en el caso de math

def operacion(numero, operacion = math.sqrt):
    return operacion(numero)

result = operacion(5)

print(result)

# Misceláneas de funciones (comúnes en lenguajes modernos)

def sumar(n1,n2 = 5):
    return n1 + n2

misc_func = {
    "sqrt": math.sqrt,
    "tan": math.tan,
    "sin": math.sin,
    "sumar": sumar
    }

def operacion(numero, operacion_base = "sqrt"):
    if operacion_base not in misc_func.keys():
        print("Error")
        return None
    
    else:
        operacion = misc_func[operacion_base]
    
    return operacion(numero)

result = operacion(5)

print(result)

# Notacion de asterisco para funciones

def minimum(*n):    # El asterisco indica que todo lo que entra pasa a ser parte de una tupla
    print(n)
    
minimum(1,5,5,6,7,50.5,-5)

# Versión verbosa
def maximum(*n):
    if len(n) == 0:
        return None
    mn = n[0]
    for value in n:
        if value > mn:
            mn = value
            
    print(mn)

maximum(1,3,5,5,99,40)

# Versión simplificada
def maximum(*n):
    mn = max(n)
    print(mn)
    
    # print(max(n))

maximum(1,3,5,5,99,40)

# Dobe asterisco

data = {"nombre":"Juan", "apellido":"Bohorquez"}

def print_data(nombre):
    print(nombre)

# print_data(**data) # Es lo mismo que pasar print_data(nombre = "Juan", apellido = "Bohorquez")

# La forma de recibir cualquier valor en diccionarios
def print_data(nombre, **other):
    print(nombre)
    print(other)

print_data(**data)

# Se deben usar los dos asteriscos tanto en la definición de la función como en la llamada de la misma

# Ejemplo 1
def math_op(*numero, operacion_base = "sqrt"):
    if operacion_base not in misc_func.keys():
        print("Error")
        return None
    else:
        operacion = misc_func[operacion_base]
    
        for i in numero:
            print(f"{operacion_base}({i}): {operacion(i)}")

math_op(1,3,5,3,6, operacion_base = "sin")
    
# Ejemplo 2
def fun(math_operation, number, **other):
    return math_operation(number)

data = {"math_operation": math.sqrt, "number": 100, "name": "juan"}

fun(**data)
fun(math_operation = math.sqrt, number = 100)

def suma(a,b,*c):
    resultado = a+b
    
    for i in c:
        resultado += i
    
    return resultado

print(suma(1,2,3,8,9,7))
    


