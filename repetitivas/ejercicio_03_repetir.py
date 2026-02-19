"""//Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
// y la media de todos los números introducidos."""

suma=0
cont=0

while True:
	num=int(input("Número (0 para salir): "))
	suma=suma+num

	if num!=0:
		cont=cont+1
	else:
		break
if cont!=0:
	media=suma/cont
else:
	media=0
print("La suma es ", suma)
print("La media es ", media)
