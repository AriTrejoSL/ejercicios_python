"""El director de una escuela está organizando un viaje de estudios, y requiere 
//determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
//viajes por el servicio. La forma de cobrar es la siguiente: 
//si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
//de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
//y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
//sin importar el número de alumnos. """

numAl=int(input("¿Cuántos alumnos participan en la actividad? "))

if numAl>=100:
	costeA=65
elif numAl>=50 and numAl<=99:
	costeA=70
elif numAl>=30 and numAl<=49:
	costeA=95;
elif numAl<30 and numAl>0:
	costeA=4000/numAl
if numAl>0:
	costeAuto=numAl*costeA
	print("El coste por alumno es ", costeA, " euros")
	print("El coste del autobús es ",costeAuto, " euros")
else:
	print("El número de alumnos debe ser un valor positivo")


