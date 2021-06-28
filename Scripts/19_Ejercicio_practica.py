# -*- coding: utf-8 -*-
"""
Created on Thu May 27 21:14:47 2021

@author: Juan Diego Bohórquez
"""

# Ud ha sido encargado de crear un sistema que sirva cómo insumo para recurso humano
# en aras de encontrar posibles problemas de salud dentro de los empleados,así cómo
# procesamiento de datos basado en fecha de ingreso en otro script en el cual no participas.
# Para esto, se le proporcionan las siguientes listas:

# 1. Una lista con la edad de los empleados
# 2. Una lista con los nombres del empleado
# 3. Una lista con la fecha de ingreso del empleado en formato mes/dia/año hora:minuto AM/PM
# 4. Una lista con el índice de masa corporal
# 5. Una lista que indica si la persona tiene o no comorbilidades

# El indice de masa corporal responde a lo siguiente
# Composición corporal 	    Índice de masa corporal (IMC)
# Peso inferior al normal 	    Menos de 18.5
# Normal                  	    Mayor o igual a 18.5 – menor a 25
# Peso superior al normal 	    Mayor o igual a 25.0 – menor a 30
# Obesidad 	                    Máyor o igual de 30.0

# Problema:
# Tu script debe entregar una lista de diccionarios, con las siguientes llaves:
# 1. name que guardará el nombre completo de la persona
# 2. date que tendrá que guardar la fecha de entrada en formato
# año-mes(en letras, completo)-dia hora(formato militar):minuto
# 3. corporal_comp que guardará la composicion corporal del IMC
# 4. risk que guardara un booleano, en verdadero, si se cumple:
#     a. Que la composicion corporal no sea normal
#     b. Que tenga comorbilidades
#     c. Que su edad sea mayor a 45 años
# 5. age con la edad de la persona

result = [
    {
        "name": "jose garcia",
        "age": 30,
        "risk": False,
        "date": "2020-March-05 23:59",
        "corporal_comp": "Normal",
    }
]

# los scripts de abajo serviran para que tengas listas de prueba
import random
import time
from datetime import datetime

def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, "%m/%d/%Y %I:%M %p", prop)

ages = [random.randint(18, 65) for i in range(1, 50)]
names = [
    random.choice(["jose", "wendy", "betsy", "carolina", "gonzalo"])
    + " "
    + random.choice(["garcia", "delgado", "martinez", "jaimes", "riveros"])
    for i in range(1, 50)
]

imc = [round(random.random() * 100, 2) for i in range(1, 50)]

begin_dates = [
    random_date("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random())
    for i in range(1, 50)
]


comorbilities = [random.choice([True, False]) for i in range(1, 50)]


print(ages, names, imc, begin_dates, comorbilities, sep="\n\n")


# --- funciones
# procesar el imc y que entregue la composición corporal
# args --> imc: float
# return --> corporal_comp: str

def get_corporal_comp(imc: float):
    """ Retorna la composición corporal dado el indice de masa
    
    Parameters
    ----------
    imc : float
        Indice de masa corporal en valor numérico.

    Returns
    -------
    indice_imc : str
        Indice de masa corporal como texto (inferior, normal, superior, obesidad).
    """
    if 0 > imc < 18.5:
        corporal_comp = "Peso inferior al normal"
    elif 18.5 > imc < 25:
        corporal_comp = "Normal"
    elif 25 > imc < 30:
        corporal_comp = "Peso superior al normal"
    else:
        corporal_comp = "Obesidad"        

    return corporal_comp

# procesar la fecha
# args --> fecha: str [formato mes/dia/año hora:minuto AM/PM] 06/28/2008 02:13 PM
# return --> fecha:str [año-mes(en letras, completo)-dia hora(formato militar):minuto]

def get_date(date_str: str):
    """Retorna la fecha en el formato deseado

    Parameters
    ----------
        fecha (str): Ingresa la fecha de la forma 06/28/2008 02:13 PM

    Returns
    -------
        str: Fecha en formato 2008-June-28 14:13
    """
    date = datetime.strptime(date_str, "%m/%d/%Y %I:%M %p")    # Recibe la fecha en el formato determinado
    new_date = date.strftime("%Y-%B-%d %H:%M")  # Transforma la fecha al formato deseado
    
    return new_date     # Devuelve la fecha cambiada como str

# procesar el riesgo
# args --> corporal_comp:str, age:int, comorbility:bool
# return --> risk: bool
# 4. risk que guardara un booleano, en verdadero, si se cumple:
#     a. Que la composicion corporal no sea normal
#     b. Que tenga comorbilidades
#     c. Que su edad sea mayor a 45 años

def get_risk(corporal_comp:str, age:int, comorbility: bool):
    """Retorna el riesgo de la persona

    Args:
        corporal_comp (str): Composicion corporal, se obtiene de la función get_corporal_comp(), posibles entradas: 
        "Peso inferior al normal", "Normal" "Peso superior al normal" y "Obesidad"
        age (int): Edad de la persona
        comorbility (bool): Comorbilidades existentes para la persona

    Returns:
        [bool]: Riesgo de la persona en forma boleana
    """
    if corporal_comp != "Normal" and age > 45 and comorbility ==  True:
        risk = True 
    else:
        risk = False

    return risk

# funcion para ordenar los datos
# funcion que me retorne un diccionario para una persona con las llaves name, risk, date, age, corporal_comp
# args --> name:str, date:str, age:int, corporal_comp:str, risk: bool
# return --> person_dict: {}
#     {
#         "name": "jose garcia",
#         "age": 30,
#         "risk": False,
#         "date": "2020-March-05 23:59",
#         "corporal_comp": "Normal",
#     }

def personal_dict_generator(name: str, age: int, risk: bool, date: str, corporal_comp: str):
    
    lista_dict ={
            "name": name,
            "age": age,
            "risk": risk,
            "date": date,
            "corporal_comp": corporal_comp,
    }
    
    return lista_dict

# funcion para iterar las listas
# reciba datos
# args --> ages: list, names: list, begin_date: list, comorbilities: list, imc: list
# return --> result_total: list

# Crear un arreglo para guardar los resultados
# Funcionalidades:
# Recorrer las listas
# Extraer la información: personal_age, personal_date, personal_name, personal_comor, personal_imc

def iter_list(ages: list, names: list, begin_date: list, comorbilities: list, imc: list):
    new_list = []
    
    for i in range(0, len(names)):
        # Definición de los datos de ingreso
        personal_age = ages[i]
        personal_name = names[i]
        personal_date = begin_date[i]
        personal_comor = comorbilities[i]
        personal_imc = imc[i]
        
        # Extraer personal composition --> get_corporal_comp(personal_imc)
        personal_comp = get_corporal_comp(personal_imc)
        
        # Extraer riesgo --> get_risk()
        risk = get_risk(personal_comp, personal_age, personal_comor)
        
        # Extraer date --> get_date()
        new_date = get_date(personal_date)
        
        # Create personal_dict() --> personal_dict_generator()
        personal_dict = personal_dict_generator(personal_name, personal_age, risk, new_date, personal_comp)
        
        # Guardar los nuevos resultados
        new_list.append(personal_dict)

    return new_list
    
print(iter_list(ages, names, begin_dates, comorbilities, imc))


