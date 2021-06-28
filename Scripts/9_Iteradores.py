# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:15:54 2021

@author: Juan Diego Bohórquez
"""

n = 10

while n > 1:
    print(n)
    n = n-1


n = int(input("Ingrese un numero: "))

# if n not in range(1,11):
#     print("Error")
# else:        
#     while n >= 1:
#         calc = n**2
#         print(calc)
#         n -= 1

while n in range(1,11):
    calc = n**2
    print(calc)
    n -= 1
else:
    print("Error")

#
#
# Bucles for
#
#

for i in range(1,10):
    print(i)

# Sugar syntax

[i for i in range(1,10)]
    
# Ejemplo
    
name = "jose" 
resultado = False
n = 0

for value in ["jose", True, "jose", "Lopez", 6]:
    if name == value:
        n += 1
        resultado = True

if resultado:
    print("el nombre está {} veces".format(n))
else:
    print("El resultado no está")
    


