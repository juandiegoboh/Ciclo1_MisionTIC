# -*- coding: utf-8 -*-
"""
Created on Fri May 21 20:23:13 2021

@author: Juan Diego Bohórquez
"""

# for i in range(1,3):
#     for j in range(1,10):
#         print(f"i: {i}, j: {j}")

"""
A prime number (or a prime) is a natural number greater than 1 that has no positive divisors 
other than 1 and itself. A natural number greater than 1 that is not a prime number 
is called a composite number.

Based on this definition, if we consider the first 10 natural numbers, we can see that 2, 3, 5, 
and 7 are primes, while 1, 4, 6, 8, 9, 10 are not. In order to have a computer tell you 
if a number N is prime, you can divide that number by all natural numbers in the range [2, N ). 
If any of those divisions yields zero as a remainder, then the number is not a prime.

Write a program to find all the primes numbers from 1 to N, where N is an integer given by the user.
Write two scripts, one using while and other one using for
"""

# n = int(input("Ingrese un numero a evaluar: "))
# resultado = []

# if n <=2:
#     print("No hay numeros primos en el rango seleccionado")

# else:
    
#     for number in range(2,n):   # For de los numeros
#         is_prime = True
#         for divisor in range(2,number):    # For de los divisores, va hasta el numero que se esta analizando
#             if number % divisor == 0:
#                 is_prime = False
#                 break
#         if is_prime == True:
#             resultado.append(number)
            
#     print(f"Los primos son {resultado}")

"""
Imprimir las siguientes figuras usando while y for

Figura 1

******
*****
****
***
**
*

Figura 2

******
*****
****
***
**
*
**
***
****
*****
******
"""

# for i in reversed(range(1,7)):  # Figura 1
#     print('*'*i)

# # Figura 2
# for i in reversed(range(1,7)):  
#     print('*'*i)
# for i in (range(2,7)):
#     print('*'*i)

# # Figura 2
# n = 6
# while n > 1:
#     print("*"*n)
#     n -= 1  

# while n <= 6:
#     print("*"*n)
#     n += 1


"""Dadas dos listas, imprime el nombre junto con la edad de la persona
Jose 29
Diana 28
Hacer dos scripts, uno usando for y otro usando while
"""

people = ["Jonas", "Julio", "Mike", "Mez"]
ages = [25, 30, 31, 39]

# Solución 1
for nombre, edad in zip(people,ages):
    print(f"{nombre} {edad}")

#Solución 2
for i in range(0,len(people)):
    nombre = people[i]
    edad = ages[i]
    print(f"{nombre} {edad}")


contador = 0
while contador < len(people):
    nombre = people[contador]
    edad = ages[contador]
    contador += 1
    print(f"{nombre} {edad}")



