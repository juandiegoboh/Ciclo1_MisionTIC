# -*- coding: utf-8 -*-
"""
Created on Mon May 24 21:54:57 2021

@author: Juan Diego Bohórquez
"""

from itertools import count
from itertools import compress
from itertools import permutations

for n in count(5,3):
    if n > 20:
        break
    print(n)


data = range(0, 10)

even = [1, 0] * 10
odd = [0, 1] * 10

even_numbers = list(compress(data, even))

print(list(permutations('ABC')))

