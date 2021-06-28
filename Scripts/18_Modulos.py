# -*- coding: utf-8 -*-
"""
Created on Wed May 26 21:23:06 2021

@author: Juan Diego Bohórquez
"""

# import <module_name>

import math
result = math.exp(1)
print(result)

# from <module_name> import <function>

from math import exp
result = exp(1)
print(result)

# from <module_name> import <function_1>, <function_2>, ...

from math import exp, sqrt, cos
print(exp(1), sqrt(2), cos(0.3))

# from <module_name> import <function> as <new_name>

from math import exp, sqrt as raiz_cuadrada, cos
print(exp(1), raiz_cuadrada(2), cos(0.3))

# from <module_name> import *

from math import *
print(tanh(2), acos(0.7))

