# -*- coding: utf-8 -*-
"""
Created on Thu May 27 20:18:51 2021

@author: Juan Diego Bohórquez
"""
"""
Write a Python program to convert a string to datetime.
Sample String : Jan 1 2014 2:43PM
Expected Output : 2014-07-01 14:43:00

strptime()
"""

from datetime import datetime as dt
from datetime import timedelta

fecha = input("Ingrese la fecha (Jan 1 2014 2:43PM): ")

def cambio_formato(fecha):
    
    date = dt.strptime(fecha, "%b %d %Y %I:%M%p")
    
    return date.strftime("%Y-%m-%d %H:%M:%S")

resultado = cambio_formato(fecha)
print(resultado)

var = dt.now()

"""
Write a Python program to subtract five days from current date.
Sample Date :
Current Date : 2015-06-22
5 days before Current Date : 2015-06-17
"""
current_date = input("Ingrese una fecha: ")
day = int(input("Ingrese el número de días a restar: "))

def substract(current_date, day=5):
    date = dt.strptime(current_date, "%Y-%m-%d")
    resta = date - timedelta(days= day)
    return resta

resultado = substract(current_date, day)
print(resultado)