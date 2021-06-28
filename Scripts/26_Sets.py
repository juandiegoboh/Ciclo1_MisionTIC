# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 11:22:30 2021

@author: Juan Diego Bohórquez
"""

my_set = {1,2,3,4,5,6, True, "juan", 3.67, -8} 
print(my_set)

my_set = {1,2,3,4,5,1,2,3,4,5,1,6,1,2}  
print(my_set)

my_list = ["Jose", "Jose", "Juan", "Juan", "Carolina"]
my_set = set(my_list)

x1 = {"foo", "baz", "bar"}
x2 = {"qux", "baz", "quux"}

# Union
union = x1.union(x2)
print(union)

union = x1 | x2
print(union)

# Interseccion
intersect = x1.intersection(x2)
print(intersect)

intersect = x1 & x2
print(intersect)

# Diferencia
diff = x1.difference(x2)
print(diff)

diff = x2.difference(x1)
print(diff)

diff = x1 - x2
print(diff)

diff = x2 - x1
print(diff)

# Diferencia simetrica

diff_sym = x1.symmetric_difference(x2)
print(diff_sym)

diff_sym = x1 ^ x2
print(diff_sym)

x1 = {"foo", "bar", "qux"}
x2 = {"foo", "bar"}

print(x2.issubset(x1))
print(x1.issuperset(x2))

x1 = {1, 2}

# Error
# x1[0]

print(x1)

x1.update([3, 4, 5])
print(x1)

my_list = list(x1)
print(my_list[0])

x = dict(name = "John", age = 36, country = "Norway")

# tuples --> inmutables, allows repeated elements
# lists --> mutables, allows repeated elements
# sets --> mutables, allows repeated elements


