# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:16:40 2021

@author: Juan Diego Bohórquez
"""

# Determine if a student can access a government subsidy to access to school education
# There are 3 requirements:
    
# 1. Must live at least at less than 40km to the round of school
# 2. Have more than 2 siblings
# 3. Family income must be lower than 1000 dollars.

distance = float(input("How far do you live from the school (km): "))
siblings = int(input("How many siblings do you have? "))
income = float(input("What is the average income of your family? (dollars) "))

# if distance in range (1,41):
#     if siblings >= 2:
#         if income < 1000:
#             print("Allowed")
#         else:
#             print("Not allowed")
#     else:
#         print("Not allowed")
# else:
#     print("Not allowed")

# Operadores ternarios, se resume el código
resultado = "Allowed" if distance in range (1,41) and siblings >= 2 and income < 1000 else "Not allowed"
print(resultado)

"""
*************************************************
"""

# Ejercicio codechef

retiro = int(input("Cuanto desea retirar?: "))
balance = float(input("Cuanto dinero hay en la cuenta?: "))
costo = 5
calculo = ((balance - retiro) - costo)

# Solución ternarios
resultado = calculo if (retiro % 5 == 0) and calculo >= 0 else balance
print(resultado)

# Solución 2
if (retiro % 5 == 0) and calculo >= 0:
    print(calculo)
else:
    balance

"""
*************************************************
"""

# Game

print("Instructions: You are in a dark room, you should choose one of two doors (identified by 1 and 2)")
print("You have 2 options, which door do you want to see? \n1. Door 1 \n2. Door 2")

n = int(input("Choose an option: "))

# while n not in [1,2]:
#     print("Not valid.")
#     n = int(input("Choose an option: "))

if n == 1:      # Door 1
    print("\nThis door contains a giant bear eating cheese cake.\nOptions: \n1. Take the cake\n2. Scream at the bear")
    
    n_2 = int(input("Choose an option: "))
    
    if n_2 == 1:
        print("The bear eats your face off, Good Job!")
    elif n_2 == 2:
        print("The bear eats your legs off, Good Job!")
    else:
        print(f"Well doing, option {n_2} is probably better. Bear runs away!")

elif n == 2:    # Door 2
    print("\nYou stare into the endless abyss at Cthulhu's retina.")
    print("What is your insanity? \n1. Blueberries \n2. Yellow Jacket clothespins \n3. Understanding revolvers yelling melodies\n")
    
    n_3 = int(input("Choose an option: "))
    
    if n_3 == 1 or 2:
        print("Your body survives powered by a mind of jello.")
    elif n_3 == 3:
        print("Good Job!")   
    else:
        print("The insanity rots of your eyes into a pool of muck, Good Job!")

else:       # Another door
    print("You stumble around and fall on a knife and die. Good Job!")











