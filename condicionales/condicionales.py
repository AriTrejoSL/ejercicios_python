#Condicionales con Python
#if, else, elif

"""
if exp_bool:
	instrucciones

if exp_bool:
	instrucciones
else:
	instrucciones

if exp_bool:
	instrucciones
elif expo_bool:
	instrucciones
else expo_bool:
	instrucciones
"""

print("Inicio")
numero=int(input("Ingresa un numero: "))

if numero>0:
	print("Es un numero positivo")
elif numero==0:
	print("Es cero")
else:
	print("Es un numero negativo")

print("Fin")