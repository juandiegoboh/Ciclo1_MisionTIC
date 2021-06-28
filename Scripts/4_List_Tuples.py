# -*- coding: utf-8 -*-
"""
Created on Fri May  7 20:54:23 2021

@author: Juan Diego Bohórquez
"""

my_list = ["jose","garcia","garcia","garcia","garcia",True]
print(my_list)

my_list.remove("garcia")    #Solo remueve el primer coincidente
print(my_list)

my_list = ["jose","garcia","medina","rocha","lopez",True]
my_bool = my_list.pop()     #Se extrae el valor más a la derecha de la lista
print(my_list)
print(my_bool)

my_bool = my_list.pop(2)    #Se extrae el indice 2 de la lista
print(my_list)
print(my_bool)

"""
Diccionarios
"""

my_dict = {"key-1":1, "key_2":2, "key_2":3}
print(my_dict)


my_dict = {"name":"Juan", "surname":"Bohorquez", "email":"juandiegoboh@hotmail.com"}
print(my_dict["name"])
print(my_dict["surname"])

my_dict = {"name":"Juan", "surname":"Bohorquez", "class_scores":[5, 1, 2, 3, 5]}
note = my_dict["class_scores"][2]
print("The Juan's note is {}".format(note))

my_dict = {"name":"Juan", "surname":"Bohorquez", 
           "class_scores":{"day_1":5, "day_2":1, "day_3":2, "day_4":3, "day_5":5}}

note = my_dict["class_scores"]["day_3"]
print("The Juan's note is {}".format(note))

