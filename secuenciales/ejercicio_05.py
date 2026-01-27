#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.

print("Conversion de grados Farenheit a grados Celsius")
farenheit=float(input("Ingresa los grados Farenheit: "))
celsius=(farenheit-32)*(5/9)

print("Los grados Farenheit son:", farenheit,"°F")
print("Los grados Celsius son:", celsius,"°C")

print(f"Los grados {farenheit}°F equivalen a {celsius}°C")