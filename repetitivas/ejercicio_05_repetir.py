"""Algoritmo que pida caracteres e imprima 
'VOCAL' si son vocales y 'NO VOCAL' 
//en caso contrario, el programa termina 
cuando se introduce un espacio."""

import math

while True:
	car=input("Introduce un caracter: ")
	if len(car) > 1:
		break
	if car==" ":
		break

	mayus=car.upper()

	if mayus=="A" or mayus=="E" or mayus=="I" or mayus=="O" or mayus=="U":
		print("Vocal")

	else: 
		print("No vocal")
