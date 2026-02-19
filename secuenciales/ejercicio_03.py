"""Dados los  catetos de un triangulo rectangulo
calcular su hipotenuso"""
import math


cateto1=float(input("Ingresa el primer cateto: "))
cateto2=float(input("Ingresa el segundo cateto: "))
hipotenusa=math.sqrt(cateto1**2 + cateto2**2)
print("La hipotenusa es ", hipotenusa)