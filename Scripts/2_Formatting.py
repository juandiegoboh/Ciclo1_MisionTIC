# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:09:10 2021

@author: Juan Diego Bohórquez
"""

my_name = "Juan"
my_surname = "Bohorquez"

print(f"{my_name} {my_surname}")
print("{} {}".format(my_name, my_surname))

formatter = "{} {} {} {}"
print(formatter.format("Jose","tiene","dos","gatos","y","un","cafe"))
# print(formatter.format("Jose","tiene","dos")) --> error porque falta una palabra que llene el espacio de la variable

meses = ["January","February","March","April","May","June","July","August","September"
         "October","November","December"]

#print("{:.3} {:.3} {:.3} {:.3} {:.3} {:.3} {:.3} {:.3} {:.3} {:.3} {:.3}".format(*meses))

for i in meses:
    print("{:.3}".format(i), end=' ')   #Use end to define how the string will end

name = "Juan Diego"
email = "juandiegoboh@hotmail.com"
address = "Cra 8w N0 62-48"
city = "Bucaramanga"
print(f"Name: {name}\nEmail: {email}\nAddress: {address}\nCity: {city}")

name = input("Please write your name: ")

print("Your name is",name)
print(f"Your name is {name}")

#Start
print("====Registration Form====")
name = input(str("Please write your name: "))
surname = input(str("Please write your surname: "))
email = input(str("Please write your email: "))
city = input(str("Please write your city: "))

print(f"\nYour account:\nName: {name}\nSurname: {surname}\nEmail: {email}\nCity: {city}")


