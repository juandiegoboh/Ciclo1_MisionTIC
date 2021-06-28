# -*- coding: utf-8 -*-
"""
Created on Sun May 30 10:36:44 2021

@author: Juan Diego Bohórquez
"""
from math import *
from collections import Counter

# Función que clasifique los huevos.

def tipo_huevo(peso: float):
    """
    Función que retorna la clasificación del huevo según su peso, usando una clasificación constante.

    Parameters
    ----------
    peso : float
        Lee el peso de un huevo.

    Returns
    -------
    tipo : str
        Retorna el tipo de huevo según la clasificación ("A", "AA", "AAA", "BC")
    """
    if 0 < peso < 53:
        tipo = "BC"   
        return tipo           
    elif 55 <= peso < 60:
        tipo = "A"
        return tipo           
    elif 60 <= peso < 69:
        tipo = "AA"
        return tipo           
    elif peso >= 69:
        tipo = "AAA"    
        return tipo   

# Función que genere una lista con los tipos de huevos

def lista_tipo_huevo(lista_pesos: list):
    """
    Retorna una lista con los tipos de huevos según la clasificación

    Parameters
    ----------
    lista_pesos : list
        Lista de pesos de huevos (gramos).

    Returns
    -------
    lista_huevos : list
        Lista del mismo tamaño que la de entrada, con la clasificación de cada huevo.

    """
    lista_huevos = []
    for i in lista_pesos:
        elemento = tipo_huevo(i)
        lista_huevos.append(elemento)

    return lista_huevos

# Función que cuente cuantos huevos hay por cada clase. Debe recibir una lista con los huevos por clase

def contar_huevos(lista_huevos: list):
    """
    Retorna una tupla con dos listas, cuenta cuantos huevos hay por cada clasificación

    Parameters
    ----------
    lista_huevos : list
        Lista de str con la clase de huevos.

    Returns
    -------
    lista_tipos : list
        Lista que retorna las clases de huevos que hay (unico valor por cada una).
    lista_cantidad : list
        Lista con un int que representa el número de huevos por cada clase.

    """
    lista_tipos = ["A", "AA", "AAA", "BC"]
    
    huevos_A = lista_huevos.count("A")
    huevos_AA = lista_huevos.count("AA")
    huevos_AAA = lista_huevos.count("AAA")
    huevos_BC = lista_huevos.count("BC")
    
    lista_cantidad = [huevos_A, huevos_AA, huevos_AAA, huevos_BC]
    
    # lista_huevos = sorted(lista_huevos)
    # cantidad_huevos = Counter(lista_huevos)   # Manera alterna, para cualquier numero de clasificaciones

    # lista_tipos = list(cantidad_huevos.keys())
    # lista_cantidad = list(cantidad_huevos.values())

    return lista_tipos, lista_cantidad


def calcular_bandejas(tipo_huevo: list, numero_huevo: list):
    """
    Calcula el numero de bandejas en las que cabe la cantidad de huevos ingresada.

    Parameters
    ----------
    tipo_huevo : list
        Lista con los tipos de huevos.
    numero_huevo : list
        Lista con el numero de huevos por tipo.

    Returns
    -------
    numero_bandejas : TYPE
        Numero de bandejas por cada tipo de huevo según su numero.

    """
    
    numero_bandejas = []
    
    for tipo, numero in zip(tipo_huevo, numero_huevo):
        
        if tipo in ("A", "BC"):
            bandejas = floor(numero/30)
        elif tipo == "AA":
            bandejas = floor(numero/24)
        elif tipo == "AAA":
            bandejas = floor(numero/12)
       
        numero_bandejas.append(bandejas)
                    
    return numero_bandejas
            
# Función que cree un diccionario con la información 

def diccionario_huevos(tipo_huevo: str, numero_huevos: int, numero_bandejas: int):
    
    diccionario = {
        "tipo_huevo":tipo_huevo,
        "numero_huevos":numero_huevos,
        "numero_bandejas":numero_bandejas,
        }
    
    return diccionario

# Función de clasificacion

def clasificacion_huevos(lista_pesos):
    """
    Clasifica los huevos según su peso, los cuenta y los ordena en un diccionario

    Parameters
    ----------
    lista_pesos : TYPE
        DESCRIPTION.

    Returns
    -------
    new_list : TYPE
        DESCRIPTION.

    """
    new_list = []
    
    tipos = lista_tipo_huevo(lista_pesos)
    lista_tipos, lista_cantidad = contar_huevos(tipos)   # Genera dos listas como resultado
    lista_bandejas = calcular_bandejas(lista_tipos, lista_cantidad)
    
    # Generación de diccionario
    
    for i in range(0,len(lista_tipos)):
        
        diccionarios = diccionario_huevos(lista_tipos[i], lista_cantidad[i], lista_bandejas[i])
        new_list.append(diccionarios)
    
    return new_list
