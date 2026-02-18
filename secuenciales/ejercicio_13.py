"""Realizar un algoritmo que lea un número y que
muestre su raíz cuadrada y su raíz cúbica. PSeInt no 
tiene ninguna función predefinida que 
permita calcular la raíz cúbica ¿cómo se puede calcular?"""
import math

num=int(input("Ingresa el número: "))
print("La raiz cuadrada del número es: ", math.sqrt(num))
print("La raiz cubica del numero es:", num**(1/3))