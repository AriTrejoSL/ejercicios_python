"""Escribir un algoritmo para calcular la nota final de 
n estudiante, considerando que: por cada respuesta 
correcta 5 puntos, por una incorrecta -1 y por respuestas 
en blanco 0. Imprime el resultado obtenido por el 
estudiante."""

correctas=int(input("¿Cuantas respuestas son correctas? "))
incorrectas=int(input("¿Cucantas respuestas son incorrectas? "))
puntos=correctas*5+incorrectas*(-1)

print("Los puntos son ",puntos)