#Calcular el perimetro y área de un rectángulo dada su base y su altura.

print("Cálculo de Área y Perímetro de un Rectángulo")
base = input("Ingresa la base: ")
base = int(base)

height = input("Ingresa la altura: ")
height = int(height)

area = base * height
perimeter = base + base + height + height

print("Area: ", area)
print("Perimetro: ", perimeter)