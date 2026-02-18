"""Dadas dos variables numÃ©ricas A y B, que el usuario 
debe teclear, se pide realizar un algoritmo que intercambie 
los valores de ambas variables 
y muestre cuanto valen al final las dos variables."""

A=int(input("Introduce el valor de la variable A: "))
B=int(input("Introduce el valor de la variable B: "))

aux=A 
A=B 
B=aux

print("El nuevo valor de A es: ", A)
print("El nuevo valor de B es: ", B)