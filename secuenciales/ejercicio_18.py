"""//Pedir el nombre y los dos apellidos de una 
persona y mostrar las iniciales."""

nom=input("¿Cual es tu nombre? ")
ape1=input("¿Cual es tu primer apellido? ")
ape2=input("¿Cual es tu segundo apellido? ")

ini=nom[0]+ape1[0]+ape2[0]
ini=ini.upper()

print("Las iniciales son ",ini)