"""Escribe un programa que pida una fecha (día, mes y 
año) y diga si es correcta."""

dia=int(input("Introduce el dia: "))
mes=int(input("Introduce el mes: "))
año=int(input("Introduce el año: "))

if mes in [1, 3, 5, 7, 8, 10, 12]:
	diaM=31
elif mes in [4, 6, 9, 11]:
	diaM=30
elif mes==2:
	if (year%4==0 and year%100!=0) or (year%400==0):
		diaM=29
	else:
		diaM=28
else:
	print("Fecha incorrecta (mes inválido)")
if dia<=0 or dia>diaM:
	print("Fecha incorrecta")
else:
	print("Fecha correcta")



