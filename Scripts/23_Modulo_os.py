# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 20:13:46 2021

@author: Juan Diego Bohórquez
"""
# Write a Python program to get the name of the operating system (Platform independent), information of current
# operating system, current working directory, print files and directories in the current directory
# and raises error in the case of invalid or inaccessible file names and paths.

# Módulo os

import os
import platform

def system_info():
    os_info = platform.uname() 
    operating_sys = os_info.system
    sys_version = os_info.version
    working_dir = os.getcwd()
    files_cwd = os.listdir(".")
    
    print(f"Sistema operativo: {operating_sys}\nVersión: {sys_version}\n\nCurrent Working Directory: {working_dir}\n\n Files y directorios: {files_cwd}")

system_info()

with open("23_ejemplo.txt","r") as f:
    text = f.read()
    print(text)

# with open("23_ejemplo.txt","w") as f:
#     text = f.write("Hello, jose")
#     print(text)

with open("23_ejemplo.txt","a") as f:
    f.write("Hello juan!")

"""
Ejercicio creacion de archivos

id, name, email, fecha actual
"""
import datetime
import os

informacion = {"nombre": ["Jose", "Carolina", "Juan", "Camila"],
               "email": ["test@test.com","test2@test.com","test3@test.com","test4@test.com"]}

index = []
nombres = []
email = []
get_time = []

def get_info():

    for k, v in informacion.items():
        if k == "nombre":
            for i in v:
                nombres.append(i)
        else:
            for i in v:
                email.append(i)
    
    for i in range(1,len(nombres)+1): 
        index.append(i)
    
    date = datetime.datetime.now()
    
    for i in range(1,len(nombres)+1):         
        get_time.append(date)
    
    return (index, nombres, email, get_time)
        
get_info()

archivo = "ejercicio_clase.txt"

for i, n, e, t in zip(index,nombres,email,get_time):
    with open(archivo, "a") as f:
        f.write(f"{i}, {n}, {e}, {t}\n")

# Write a Python program to list only directories, files and all directories, files in a specified path.

# Write a Python program to find the parent's process id, real user ID of the current process and
# change real user ID.

# Write a Python program to run an operating system command using the os module.



