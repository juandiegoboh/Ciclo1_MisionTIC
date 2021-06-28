# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:42:52 2021

@author: Juan Diego Bohórquez
"""

def get_max_average_price(prices_list: list):
    """Retorna el valor máximo dado una lista de precios
    Args:
        prices_list (list): Lista de precios
    Returns:
        float: valor máximo
    """
    
    maximo = max(prices_list)
    
    return maximo


def get_min_average_price(prices_list: list):
    """Retorna el valor mínimo dado una lista de precios
    Args:
        prices_list (list): Lista de precios
    Returns:
        float: valor mínimo
    """
    minimo = min(prices_list)

    return minimo


def get_max_average_volume(volume_list: list):
    """Retorna el volumen máximo dado una lista de volumenes de venta
    Args:
        volume_list (list): Lista de volúmenes
    Returns:
        float: valor máximo
    """
    volumen_maximo = max(volume_list)

    return volumen_maximo


def get_max_sale_date(dates_list: list, prices_list: list):
    """Retorna la fecha dónde se dió el máximo precio
    Args:
        dates_list (list): lista con el histórico de fechas
        prices_list (list): lista con el histórico de precios
    Returns:
        str: Fecha con histórico
    """
    max_price = get_max_average_price(prices_list)

    # Algoritmo para obtener el índice del máximo de la lista de precios acá
    
    max_index = prices_list.index(max_price)     

    return dates_list[max_index]


def get_min_sale_date(dates_list: list, prices_list: list):
    """Retorna la fecha dónde se dió el mínimo precio
    Args:
        dates_list (list): lista con el histórico de fechas
        prices_list (list): lista con el histórico de precios
    Returns:
        str: Fecha con histórico
    """
    min_price = get_min_average_price(prices_list)

    min_index = prices_list.index(min_price)

    return dates_list[min_index]


def get_max_price_type(types_list: list, prices_list: list):
    """Retorna el tipo de aguacate con el máximo precio
    Args:
        dates_list (list): lista con el histórico de fechas
        prices_list (list): lista con el histórico de precios
    Returns:
        str: Fecha con histórico
    """
    max_price = get_min_average_price(prices_list)

    max_index = prices_list.index(max_price)

    return types_list[max_index]


def build_dict(prices_list, dates_list, types_list, volumes_list):
    """Función para construir el diccionario de salida
    Args:
        prices_list (list): [description]
        dates_list (list): [description]
        types_list (list): [description]
        volumes_list (list): [description]
    Returns:
        dict: Diccionario con las llaves solicitadas
    """
    max_price = get_max_average_price(prices_list)
    min_price = get_min_average_price(prices_list)
    max_volume = get_max_average_volume(volumes_list)
    max_date = get_max_sale_date(dates_list, prices_list)
    min_date = get_min_sale_date(dates_list, prices_list)
    max_type = get_max_price_type(types_list, prices_list)

    result = {
        "precio promedio maximo": max_price,
        "precio promedio minimo": min_price,
        "volumen maximo": max_volume,
        "fecha maximo promedio": max_date,
        "fecha minimo promedio": min_date,
        "tipo con maximo precio": max_type,
    }

    return result


def get_region_data(data: dict, region: str):
    """Extrae como listas, los datos de interes que son el tipo de aguacate,
       el precio promedio, las fechas y el volumen de venta
    Args:
        data (list): Diccionario con todas las llaves de datos
        region (str): region de interés para extraer
    Returns:
        (prices_list, dates_list, types_list, volumes_list) (tuple): Resultado con las listas de datos
    """
    # Listas para almacenar resultados
    types_list = []
    prices_list = []
    dates_list = []
    volumes_list = []

    # Extrae acá la información de interés de cada llave (columna originalmente)
    region_data = data["region"]
    types_data = data["type"]
    prices_data = data["AveragePrice"]
    dates_data = data["Date"]
    volumes_data = data["Total Volume"]

    # itera los items del diccionario de region_data, extrayendo dos variables:
        
    # index, value. Dado que region_data es un diccionario, tendrás que usar items()

    # coloca el iterador acá
    
    for index,value in region_data.items():
        if value == region:
            types_list.append(types_data[index])
            prices_list.append(prices_data[index])            
            dates_list.append(dates_data[index])            
            volumes_list.append(volumes_data[index])

        # si el valor es igual a la region, añade a las listas los datos de interés, sigue el
        # ejemplo
            #types_list.append(types_data[index])
    return (prices_list, dates_list, types_list, volumes_list)


def get_general_statics(data: dict, region: str):
    # Escribe acá la instrucción para que
    # si la region NO existe dentro de los valores de la llave "region" de data, retorne None
    
    if region not in data["region"].values():
        return None
    
    else:
        prices_list, dates_list, types_list, volumes_list = get_region_data(data, region)
    
        result = build_dict(prices_list, dates_list, types_list, volumes_list)
        return result

        

print(get_general_statics({'Date': {'4664': '2016-04-17', '5746': '2017-07-16', '15251': '2017-05-14', '17174': '2017-01-29', '9665': '2015-08-16', '3140': '2016-08-07', '13542': '2016-01-17', '16419': '2017-04-30', '14748': '2017-11-12', '16659': '2017-10-22', '3464': '2016-05-15', '16194': '2017-07-30', '18141': '2018-03-25', '8586': '2018-03-25', '388': '2015-07-12', '362': '2015-01-11', '2192': '2015-11-01', '5719': '2017-01-15', '2930': '2016-08-21', '13069': '2016-02-21', '12820': '2016-12-04', '2784': '2015-06-14', '11201': '2015-02-01', '5269': '2016-08-28', '1231': '2015-04-26', '9580': '2015-04-05', '2358': '2015-08-23', '10703': '2015-08-30', '14726': '2016-04-10', '7060': '2017-10-01', '12025': '2016-03-20', '7449': '2017-05-28', '12309': '2016-10-02', '8961': '2018-03-04', '1878': '2015-11-15', '2309': '2015-08-02', '10946': '2015-12-27', '1356': '2015-11-29', '15058': '2017-01-01', '13937': '2016-06-12', '1723': '2015-11-08', '16176': '2017-12-03', '16013': '2017-12-31', '3001': '2016-04-10', '9902': '2015-01-25'}, 'AveragePrice': {'4664': 0.95, '5746': 1.48, '15251': 1.41, '17174': 1.08, '9665': 2.08, '3140': 1.17, '13542': 1.55, '16419': 2.38, '14748': 1.71, '16659': 2.48, '3464': 0.9, '16194': 1.25, '18141': 1.42, '8586': 1.08, '388': 1.18, '362': 0.92, '2192': 0.97, '5719': 0.99, '2930': 1.48, '13069': 1.44, '12820': 2.42, '2784': 0.7, '11201': 1.5, '5269': 1.12, '1231': 1.21, '9580': 1.65, '2358': 0.89, '10703': 1.92, '14726': 1.31, '7060': 1.72, '12025': 1.44, '7449': 1.32, '12309': 1.78, '8961': 1.18, '1878': 0.9, '2309': 1.14, '10946': 1.6, '1356': 0.95, '15058': 1.64, '13937': 1.16, '1723': 0.6, '16176': 1.46, '16013': 1.48, '3001': 0.82, '9902': 2.01}, 'Total Volume': {'4664': 2114990.64, '5746': 670476.49, '15251': 22296.61, '17174': 121203.53, '9665': 3554.43, '3140': 6144827.51, '13542': 10459.56, '16419': 4681.64, '14748': 2664.62, '16659': 15825.16, '3464': 952354.86, '16194': 5816.2, '18141': 163496.7, '8586': 277267.97, '388': 182856.82, '362': 6024932.34, '2192': 869927.27, '5719': 557377.82, '2930': 727279.79, '13069': 8237.96, '12820': 8036.44, '2784': 1035973.14, '11201': 4941.74, '5269': 83627.94, '1231': 65742.4, '9580': 21064.17, '2358': 5235579.44, '10703': 8005.96, '14726': 21561.29, '7060': 227535.41, '12025': 7435.68, '7449': 143674.94, '12309': 8909.48, '8961': 559943.98, '1878': 568414.35, '2309': 309611.87, '10946': 32041.32, '1356': 119919.67, '15058': 3425.49, '13937': 9568.18, '1723': 1102271.52, '16176': 5649.91, '16013': 6518.64, '3001': 86897.72, '9902': 711.52}, '4046': {'4664': 852518.35, '5746': 64407.19, '15251': 239.72, '17174': 35172.06, '9665': 378.55, '3140': 2152079.32, '13542': 6.15, '16419': 2188.24, '14748': 0.0, '16659': 1737.93, '3464': 159348.75, '16194': 228.57, '18141': 29253.3, '8586': 70493.35, '388': 23580.7, '362': 2889591.29, '2192': 214932.11, '5719': 249159.52, '2930': 68443.67, '13069': 1481.86, '12820': 103.64, '2784': 651120.92, '11201': 150.16, '5269': 24062.61, '1231': 2070.06, '9580': 112.46, '2358': 3058909.34, '10703': 3.72, '14726': 3204.95, '7060': 132184.69, '12025': 2263.17, '7449': 60061.87, '12309': 262.02, '8961': 181586.15, '1878': 83998.38, '2309': 148657.53, '10946': 3224.07, '1356': 77155.36, '15058': 8.52, '13937': 131.67, '1723': 793103.44, '16176': 85.78, '16013': 24.84, '3001': 44344.9, '9902': 59.16}, '4225': {'4664': 756238.99, '5746': 415327.9, '15251': 5966.79, '17174': 5405.54, '9665': 2654.29, '3140': 2039791.18, '13542': 248.53, '16419': 289.11, '14748': 245.71, '16659': 2304.96, '3464': 252574.36, '16194': 118.74, '18141': 5080.04, '8586': 27183.18, '388': 56317.45, '362': 2485720.1, '2192': 563719.33, '5719': 86964.23, '2930': 413651.59, '13069': 3293.97, '12820': 3639.96, '2784': 202731.92, '11201': 3819.72, '5269': 18386.73, '1231': 42192.26, '9580': 20035.04, '2358': 1546628.56, '10703': 675.06, '14726': 7746.53, '7060': 21112.28, '12025': 2989.88, '7449': 29709.54, '12309': 3891.17, '8961': 241036.31, '1878': 199356.57, '2309': 64352.06, '10946': 13453.09, '1356': 9407.46, '15058': 320.56, '13937': 4168.66, '1723': 234926.57, '16176': 149.33, '16013': 333.44, '3001': 3303.93, '9902': 572.36}, '4770': {'4664': 10596.68, '5746': 5640.71, '15251': 0.0, '17174': 0.0, '9665': 0.0, '3140': 211671.11, '13542': 0.0, '16419': 0.0, '14748': 0.0, '16659': 1.66, '3464': 39117.61, '16194': 0.0, '18141': 0.0, '8586': 9616.52, '388': 35107.11, '362': 103573.42, '2192': 31481.92, '5719': 169.63, '2930': 21950.39, '13069': 0.0, '12820': 2.74, '2784': 13413.05, '11201': 0.0, '5269': 1858.09, '1231': 2780.63, '9580': 0.0, '2358': 30815.55, '10703': 0.0, '14726': 111.55, '7060': 9.0, '12025': 0.0, '7449': 1890.54, '12309': 643.79, '8961': 1031.75, '1878': 16340.66, '2309': 19051.78, '10946': 1672.35, '1356': 5435.02, '15058': 0.0, '13937': 395.0, '1723': 11555.39, '16176': 0.0, '16013': 0.0, '3001': 5340.61, '9902': 0.0}, 'Total Bags': {'4664': 495636.62, '5746': 185100.69, '15251': 16090.1, '17174': 80625.93, '9665': 521.59, '3140': 1741285.9, '13542': 10204.88, '16419': 2204.29, '14748': 2418.91, '16659': 11780.61, '3464': 501314.14, '16194': 5468.89, '18141': 129163.36, '8586': 169974.92, '388': 67851.56, '362': 546047.53, '2192': 59793.91, '5719': 221084.44, '2930': 223234.14, '13069': 3462.13, '12820': 4290.1, '2784': 168707.25, '11201': 971.86, '5269': 39320.51, '1231': 18699.45, '9580': 916.67, '2358': 599225.99, '10703': 7327.18, '14726': 10498.26, '7060': 74229.44, '12025': 2182.63, '7449': 52012.99, '12309': 4112.5, '8961': 136289.77, '1878': 268718.74, '2309': 77550.5, '10946': 13691.81, '1356': 27921.83, '15058': 3096.41, '13937': 4872.85, '1723': 62686.12, '16176': 5414.8, '16013': 6160.36, '3001': 33908.28, '9902': 80.0}, 'Small Bags': {'4664': 433889.83, '5746': 177112.27, '15251': 802.37, '17174': 76958.46, '9665': 236.67, '3140': 1616257.39, '13542': 10204.88, '16419': 1853.34, '14748': 2418.91, '16659': 1490.66, '3464': 71486.17, '16194': 5458.89, '18141': 109052.26, '8586': 140702.4, '388': 65681.23, '362': 510560.41, '2192': 58929.19, '5719': 145333.47, '2930': 203758.36, '13069': 2833.52, '12820': 4290.1, '2784': 126508.62, '11201': 903.33, '5269': 39315.7, '1231': 9812.43, '9580': 916.67, '2358': 513745.16, '10703': 7327.18, '14726': 8558.96, '7060': 61436.17, '12025': 613.33, '7449': 44354.41, '12309': 4065.29, '8961': 128164.6, '1878': 258913.25, '2309': 72040.69, '10946': 5921.08, '1356': 20470.74, '15058': 2585.1, '13937': 1665.78, '1723': 62666.63, '16176': 5225.55, '16013': 6147.77, '3001': 33662.76, '9902': 80.0}, 'Large Bags': {'4664': 52871.73, '5746': 886.2, '15251': 15287.73, '17174': 3667.47, '9665': 284.92, '3140': 89290.29, '13542': 0.0, '16419': 350.95, '14748': 0.0, '16659': 10277.06, '3464': 427648.8, '16194': 10.0, '18141': 20111.1, '8586': 20939.89, '388': 2170.33, '362': 31874.03, '2192': 845.56, '5719': 75750.97, '2930': 15197.45, '13069': 628.61, '12820': 0.0, '2784': 42198.63, '11201': 68.53, '5269': 0.0, '1231': 8286.28, '9580': 0.0, '2358': 85422.36, '10703': 0.0, '14726': 1939.3, '7060': 12793.27, '12025': 1569.3, '7449': 7658.58, '12309': 47.21, '8961': 2453.04, '1878': 2157.19, '2309': 5488.53, '10946': 7770.73, '1356': 7440.75, '15058': 511.31, '13937': 3207.07, '1723': 19.49, '16176': 189.25, '16013': 12.59, '3001': 156.09, '9902': 0.0}, 'XLarge Bags': {'4664': 8875.06, '5746': 7102.22, '15251': 0.0, '17174': 0.0, '9665': 0.0, '3140': 35738.22, '13542': 0.0, '16419': 0.0, '14748': 0.0, '16659': 12.89, '3464': 2179.17, '16194': 0.0, '18141': 0.0, '8586': 8332.63, '388': 0.0, '362': 3613.09, '2192': 19.16, '5719': 0.0, '2930': 4278.33, '13069': 0.0, '12820': 0.0, '2784': 0.0, '11201': 0.0, '5269': 4.81, '1231': 600.74, '9580': 0.0, '2358': 58.47, '10703': 0.0, '14726': 0.0, '7060': 0.0, '12025': 0.0, '7449': 0.0, '12309': 0.0, '8961': 5672.13, '1878': 7648.3, '2309': 21.28, '10946': 0.0, '1356': 10.34, '15058': 0.0, '13937': 0.0, '1723': 0.0, '16176': 0.0, '16013': 0.0, '3001': 89.43, '9902': 0.0}, 'type': {'4664': 'conventional', '5746': 'conventional', '15251': 'organic', '17174': 'organic', '9665': 'organic', '3140': 'conventional', '13542': 'organic', '16419': 'organic', '14748': 'organic', '16659': 'organic', '3464': 'conventional', '16194': 'organic', '18141': 'organic', '8586': 'conventional', '388': 'conventional', '362': 'conventional', '2192': 'conventional', '5719': 'conventional', '2930': 'conventional', '13069': 'organic', '12820': 'organic', '2784': 'conventional', '11201': 'organic', '5269': 'conventional', '1231': 'conventional', '9580': 'organic', '2358': 'conventional', '10703': 'organic', '14726': 'organic', '7060': 'conventional', '12025': 'organic', '7449': 'conventional', '12309': 'organic', '8961': 'conventional', '1878': 'conventional', '2309': 'conventional', '10946': 'organic', '1356': 'conventional', '15058': 'organic', '13937': 'organic', '1723': 'conventional', '16176': 'organic', '16013': 'organic', '3001': 'conventional', '9902': 'organic'}, 'year': {'4664': 2016, '5746': 2017, '15251': 2017, '17174': 2017, '9665': 2015, '3140': 2016, '13542': 2016, '16419': 2017, '14748': 2017, '16659': 2017, '3464': 2016, '16194': 2017, '18141': 2018, '8586': 2018, '388': 2015, '362': 2015, '2192': 2015, '5719': 2017, '2930': 2016, '13069': 2016, '12820': 2016, '2784': 2015, '11201': 2015, '5269': 2016, '1231': 2015, '9580': 2015, '2358': 2015, '10703': 2015, '14726': 2016, '7060': 2017, '12025': 2016, '7449': 2017, '12309': 2016, '8961': 2018, '1878': 2015, '2309': 2015, '10946': 2015, '1356': 2015, '15058': 2017, '13937': 2016, '1723': 2015, '16176': 2017, '16013': 2017, '3001': 2016, '9902': 2015}, 'region': {'4664': 'Plains', '5746': 'BaltimoreWashington', '15251': 'CincinnatiDayton', '17174': 'SouthCentral', '9665': 'Columbus', '3140': 'California', '13542': 'NorthernNewEngland', '16419': 'Orlando', '14748': 'Albany', '16659': 'Portland', '3464': 'Denver', '16194': 'NewOrleansMobile', '18141': 'SouthCentral', '8586': 'CincinnatiDayton', '388': 'Charlotte', '362': 'California', '2192': 'SanFrancisco', '5719': 'Atlanta', '2930': 'BaltimoreWashington', '13069': 'LasVegas', '12820': 'HartfordSpringfield', '2784': 'WestTexNewMexico', '11201': 'Roanoke', '5269': 'Spokane', '1231': 'Louisville', '9580': 'Chicago', '2358': 'SouthCentral', '10703': 'NorthernNewEngland', '14726': 'WestTexNewMexico', '7060': 'NewOrleansMobile', '12025': 'Atlanta', '7449': 'Pittsburgh', '12309': 'Charlotte', '8961': 'Sacramento', '1878': 'Portland', '2309': 'SouthCarolina', '10946': 'Plains', '1356': 'Nashville', '15058': 'BuffaloRochester', '13937': 'RichmondNorfolk', '1723': 'PhoenixTucson', '16176': 'NewOrleansMobile', '16013': 'MiamiFtLauderdale', '3001': 'Boise', '9902': 'GrandRapids'}}, 'Portland'))
