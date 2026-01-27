#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a 
#cuantas horas y minutos corresponde.

minutos=int(input("Ingresa la cantidad de muinutos: "))
reshoras=(minutos//60)
resmin=minutos%60

print(f"Es igual a {reshoras} horas y {resmin} minutos")