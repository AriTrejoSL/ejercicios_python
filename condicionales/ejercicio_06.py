"""Programa que lea una cadena por teclado y compruebe si es
una letra mayuscula"""

#La función booleana .isupper valida el formato de una cadena 
#de texto, simplemente te da verdadero o falso

cadena=input("Ingresa el texto: ")

if cadena.isupper():
	print(f"{cadena} es mayuscula")
else:
	print(f"{cadena} es minuscula")