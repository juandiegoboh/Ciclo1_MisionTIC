# -*- coding: utf-8 -*-
"""
Created on Fri May 21 20:11:54 2021

@author: Juan Diego Bohórquez
"""

# Una linea de supermercados de renombre en tu país te ha contratado y encomendado la tarea de automatizar el cálculo de la suma a pagar por parte de sus clientes durante una campaña agresiva para mover inventario. La campaña consiste en dar descuentos para algunos productos de hasta el 30%. Adicionalmente, si la fecha de vencimiento del producto es el día de hoy, se aplicará un 20% adicional de descuento.

# La cadena de supermercados ya tiene un software que se encarga de registrar y ordenar los datos de los productos del cliente, utilizando listas y diccionarios, siguiendo la siguiente estructura:
    
# import json

# productos = json.loads(input())

productos = [
    {"sku": 1, "fecha_expiracion": "", "precio": 753.723, "descuento": 5}, 
    {"sku": 2, "fecha_expiracion": "hoy",        "precio": 355.885, "descuento": 2}, 
    {"sku": 3, "fecha_expiracion": "hoy", "precio": 309.222, "descuento": 0},   
    {"sku": 4, "fecha_expiracion": "hoy", "precio": 867.799, "descuento": 0}, 
    {"sku": 5, "fecha_expiracion": "hoy", "precio": 186.459, "descuento": 3}, 
    {"sku": 6, "fecha_expiracion": "hoy", "precio": 574.783, "descuento": 22}
]

import json
productos = json.loads(input())

compras = []

for i in range(0,len(productos)):
    # Precios y descuentos de los productos
    precio_p = productos[i]["precio"]
    descuento_p = productos[i]["descuento"]/100
    
    # Valor que se descuenta de cada producto
    descuento1 = (precio_p*0.2)   # Descuento si expira hoy
    descuento2 = (precio_p*(descuento_p)) # Descuento propio del producto
    descuento3 = descuento2 + (precio_p - descuento2)*0.2   # Descuento si el producto tiene descuento y vence hoy
    
    if productos[i]["fecha_expiracion"] != "hoy":
        precio = precio_p - descuento2
        compras.append(precio)
    else:
        # productos[i]["fecha_expiracion"] == "hoy" and productos[i]["descuento"] != "":
        precio = precio_p - descuento3
        compras.append(precio)

resultado = round(sum(compras),2)

print(resultado)



