"""//Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
// y la media de todos los números introducidos."""

suma=0
cont=0

num=int(input("Número (0 para salir): "))

while num!=0:
	suma=suma+num
	cont=cont+1
	num=int(input("Número (0 para salir): "))
	if cont>0:
		media=suma/cont
	else:
		media=0
print("La suma es ", suma)
print("La media es ", media)

