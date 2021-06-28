# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

# Primitives

my_char = 'a'
print(my_char)

my_int = 5
print(my_int)

my_float = 5.5
print(my_float)

my_new_int = int(my_float)
print(float(my_new_int))

#Ops

print(5*4)

print(10/5)
print(10//5)

print(11%1)

#Primitives

my_boolean_1 = True   #Boolean
my_boolean_2 = False

print(my_boolean_1)

#Boolean + math ops
my_boolean_1 = True
print(my_boolean_1/2)
print(int(True))    #Lenguaje binario
print(int(False))
print(True*False)   #Transforma lo booleanos en 1s y 0s

#String + math ops
my_char = "*"

print(my_char*10)   #Diminuye tiempo para manejar strings 
print("*"*10)
print("Jose "*100)

my_name = "Juan"
my_surname = "Bohorquez"
my_third_variable = " "

print(my_name + " " +my_surname)
print(my_name,my_surname)
print(my_name + my_third_variable + my_surname)
print(f"{my_name} {my_surname}")    #Se formatea el texto luego de escribir f""
print("{} {}".format(my_name, my_surname))  #Utilizando el método format()