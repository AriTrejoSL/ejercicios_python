"""La asociación de vinicultores tiene como política 
fijar un precio inicial al kilo de uva, la cual se 
clasifica en tipos A y B,  y además en tamaños 1 y 2. 
Cuando se realiza la venta del producto, ésta es de un 
solo tipo y tamaño, se requiere determinar cuánto recibirá 
un productor por la uva que entrega en un embarque, 
considerando lo siguiente: si es de tipo A, se le cargan 
20 céntimos al precio inicial cuando es de tamaño 1; y 30
céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 
céntimos cuando es de tamaño 1, y 50 céntimos cuando es 
de tamaño 2. """


precioI=float(input("Introduce el precio inicial por kilos de la Uva: "))
kilos=int(input("Introduce cuantos kilos has vendido: "))
tipo=input("Introduce el tipo de la Uva (A/B): ").upper()

if (tipo!="A") and (tipo!="B"):
	print("Tipo incorrecto")
else:
	tamaño=input("Introduce el tamaño de la Uva (1/2): ")
	if tamaño!="1" and tamaño!="2" :
		print("Tamaño incorrecto")
	else:
		if tipo=="A":
			if tamaño=="1":
				precioI=precioI+20
			else:
				precioI=precioI+30
		else:
			if tamaño=="1":
				precioI=precioI-20
			else:
				precioI=precioI-30

precioF=precioI*kilos
print("La ganancia es ", (precioF/100), "euros")


