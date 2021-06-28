# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:05:53 2021

@author: Juan Diego Bohórquez
"""

from collections import Counter
# Write a Python script to concatenate following dictionaries to create a new one.

# Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def crear_diccionario():
    dic1 = {1:10, 2:20}
    dic2 = {3:30, 4:40}
    dic3 = {5:50, 6:60}

    dict = dic1.copy()

    for key, value in dic2.items():
        dict[key] = value

    for key, value in dic3.items():
        dict[key] = value

    return(dict)

resultado = crear_diccionario()

print(resultado)

# Solución más corta
dic = {}
for i in [dic1,dic2,dic3]:
    print(i)
    for key, value in i.items():
        dic[key]=value

print(dic)  

# Solución con el método update

my_dict = {}
for element in [dic1,dic2,dic3]:
    my_dict.update(element)

print(my_dict)  

# Doble asterisco

my_dict = {**dic1, **dic2, **dic3}
print(my_dict)  

# Write a Python script to check whether a given key already exists in a dictionary.

# Write a Python program to iterate over dictionaries using for loops.

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n)
# in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def diccionario_cuadrado(n: int):
    diccionario = {}
    for i in range(1,n+1):
        diccionario[i] = i**2
    
    print(diccionario)

n = int(input("Ingrese un número: "))

diccionario_cuadrado(n)

# Write a Python program to sum all the items in a dictionary.
# my_dict =  {'data1':100,'data2':-54,'data3':247}

# Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

def suma_diccionarios(d1:dict, d2:dict):
    
    d3 = d1.copy()
    
    for k1, v1 in d1.items():
        if k1 not in d2.keys():
            d3[k1] = v1
        else:
            d3[k1] = v1 + d2[k1]            

    for k2, v2 in d2.items():
        if k2 not in d3.keys():
            d3[k2] = v2
            
    return d3

resultado = suma_diccionarios(d1,d2)

print(resultado)

# Metodo con el metodo counter del módulo Collections

def suma_diccionarios(d1, d2):
    resultado = Counter(d1) + Counter(d2)
    
    print(resultado)

suma_diccionarios(d1, d2)


# Write a Python program to print all unique values in a dictionary list.
sample = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

def unique_values(dic: list):
    uniques = []
    for i in dic:
        for k, v in i.items():
            uniques.append(v)

    uniques = set(uniques)    

    return uniques 
        
resultado = unique_values(sample)

print(resultado)



# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}