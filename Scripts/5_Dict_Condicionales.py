# -*- coding: utf-8 -*-
"""
Created on Tue May 11 20:14:38 2021

@author: Juan Diego Bohórquez
"""
import random

words = ["piedra","papel","tijera"]
print(random.choice(words))

# Si yo tengo un diccionario con piedra, papel o tijera, como escojo un elemento de manera
# aleatoria.

my_dict = {"word-1":"piedra", "word-2":"papel", "word-3":"tijera"}

words = random.choice(list(my_dict.keys())) #Se vuelve lista el grupo de llaves, y se escoge aleatoriamente
print(my_dict[words])

words = random.choice(list(my_dict.values())) #Se vuelve lista el grupo de llaves, y se escoge aleatoriamente
print(words)

"""
Condicionales
"""

number = 25

if number ==5:
    print("Es cinco")
else:
    print("Es diferente de cinco")

print("Finalizado")

# Write a program that ask to the user for a number, if the number is divisible by 5, print "es divisible por 5"
# else, print "No es divisible"

number = int(input("Please enter a int number: "))

if number % 5 == 0:
     print("Es divisible por 5")
else:
     print("No es divisible por 5")
     
# ****************************************
# elif conditional
number = int(input("Ingrese un número: "))

if number == 0:
    print("El número ingresado es 0.")
    
elif number >  0:
    print("El número {} es positivo.".format(number))

elif number < 0:
    print("El número {} es negativo.".format(number))
else:
    print("Error")

# ========================================
# Gender ---> F, M; gender cannot be empty
# email ---> cannot be empy
# Write a program that print "invalido" if the gender is not F, M, or if the email or the 
# gender are empy, else print "valido"
# The email must contain '@'

gender = input("Insert your gender (F or M): ")
email = input("Please write your email: ")

gender = gender.upper()

if gender == "":
    print("Invalido")
elif gender == "F" or "M":
    print("El género ingresado ({}) es válido".format(gender))
else:
    print("Invalido")    

if email == "":
    print("Invalido")
elif email.find('@') == -1:
    print("Invalido")
else:
    print("El email ingresado ({}) es válido".format(email))    



