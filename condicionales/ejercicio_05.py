"""Escribe un rograma que pida un nombre de usuario y una contraseña
y si se ha introducido "pepe" y "asdasd" se indica "Has entrado
al sistema", si no se da un error"""

#usuarioR="pepe"
passwordR="asdasd"

usuarioI=input("Ingresa el usuario: ")
passwordI=input("Ingresa la contraseña: ")

if usuarioI=="pepe" and passwordI==passwordR:
	print("Has entrado al sistema")
else:
	print("Usuario y contraseña incorrectos")

