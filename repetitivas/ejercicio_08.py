"""Escribe un programa que pida el limite inferior y 
superior de un intervalo. Si el límite inferior es mayor 
que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que 
introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
* La suma de los números que están dentro del intervalo 
(intervalo abierto).
* Cuantos números están fuera del intervalo.
* He informa si hemos introducido algún número igual a los 
límites del intervalo."""

sumaDI=0
contFI=0
igualLim=False

while True:
	limI=int(input("Introduce el límite inferior del intervalo: "))
	limS=int(input("Introduce el límite superior del intervalo: "))
	if limI>limS:
		print("ERROR: El límite inferior debe ser menor que el superior.")
	else:
		break
num=int(input("Introduce un número (0 para salir): "))

while num!=0:
	if num>limI and num<limS:
		sumaDI=num
	else:
		contFI+=1

	if num==limI or num==limS:
		igualLim=True
	num=int(input("Introduce un número (0 para salir): "))
		
print("La suma de los números dentro del intervalo es ", sumaDI)
print("La cantidad de números fuera del intervalo  es ", contFI)

if igualLim:
	print("Se a introducido algún número igual a los límites del intervalo")
else:
	print("No se ha introducido ningún número igual a los límites del intervalo.")

