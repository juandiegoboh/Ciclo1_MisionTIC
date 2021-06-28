# -*- coding: utf-8 -*-
"""
Created on Wed May 26 21:31:06 2021

@author: Juan Diego Bohórquez
"""

import datetime

date = datetime.date.today()

print(date)
print(date.year, date.month, date.day)
print(date.isoformat())

date = datetime.datetime.now()

print(date)
print(date.hour, date.minute)
print(date.strftime("%y/%B/%d"))

"""
Write a Python script to display the various Date Time formats
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
"""

def formato_fecha():
    from datetime import datetime as dt
    
    date = dt.now()

    a = date
    b = date.year
    c = date.strftime("%B")
    d = date.strftime("%U")
    e = date.strftime("%A")
    f = date.strftime("%j")
    g = date.strftime("%d")
    h = date.strftime("%w")
    
    print(f"a) Current date and time: {a} \nb) Current year: {b} \nc) Month of year: {c} \nd) Week number of the year: {d} \ne) Weekday of the week: {e} \nf) Day of year: {f} \ng) Day of the month: {g} \nh) Day of week: {h}")

formato_fecha()
