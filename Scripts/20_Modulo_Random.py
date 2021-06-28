# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 20:53:18 2021

@author: Juan Diego Bohórquez
"""
import random
import string
# Generate 3 random integers between 100 and 999 which is divisible by 5

def random_numbers():
    for i in range(1,4):
        numero = random.randrange(100,1000,5)
        
        print(f"Número aleatorio {i}: {numero}")

random_numbers()

# Random Lottery Pick. Generate 1000 random lottery tickets and pick two lucky tickets from it as a winner.
# Asks to the user for a number, and print if he is a winner or not
# 1 < N < 1000

ticket = int(input("Ingrese un número: "))

def generador_loteria(total_tickets = 100):
    
    numeros_loteria = []
    
    for i in range(0,total_tickets):
        numero = random.randint(0, total_tickets)
        
        numeros_loteria.append(numero)

    return numeros_loteria

def generador_ganador(numeros_loteria, ganadores = 2):
    
    n_ganadores = random.choices(numeros_loteria, k = ganadores)
    
    return n_ganadores

def revisar_ganadores(ticket):
    
    numeros = generador_loteria()
    ganadores = generador_ganador(numeros)
    
    if ticket in ganadores:
        return "Felicidades, el ticker {ticket} es ganador."
    
    else:
        return f"Lo sentimos, los números ganadores eran {ganadores}, sigue participando"

resultado = revisar_ganadores(ticket)    

print(resultado)
    
# Pick a random character from a given String

# Generate  random String of length 5.
# hint: use the string module


def random_lower_string(l = 5):
    
    lowercases = string.ascii_lowercase
    result_list = random.choices(lowercases, k=l)
    result_str = ""
    
    for char in result_list:
        result_str += char
    
    return result_str
    
resultado = random_lower_string()

print(resultado)

# Solución 2

def random_lower_string(l = 5):
    
    lowercases = string.ascii_lowercase
    result_list = random.choices(lowercases, k=l)
    result_str = "".join(result_list)   # Une el string con lo que este entre paréntesis

    return result_str

resultado = random_lower_string()

print(resultado)

# Generate a random Password which meets the following conditions:
# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

def generate_password():

    # "Biblioteca" de caracteres para construir la contraseña
    
    l_letter = random.choices(string.ascii_lowercase, k=6)
    u_letter = random.choices(string.ascii_uppercase, k=2)
    digits = random.choices(string.digits, k=1)
    symbols = random.choices(string.punctuation, k=1)
    
    # password = "".join(l_letter) + "".join(u_letter) + "".join(digits) + "".join(symbols)
    
    password_list = l_letter + u_letter + digits + symbols
    password = random.sample(password_list, k=10)
    password = "".join(password)
    
    return password

resultado = generate_password()

print(resultado) 










