# @autor: Esteban Marin Cardona
# @fecha: 15/08/2024
# @descripcion: Programa en Python que permite calcular el area y el perimetro de un triangulo rectangulo
#               ensena un mensaje si el area del triangulo es mayor o igual de 3 
#               los datos son ingresados por teclado

import math  # Importar el modulo math para usar sqrt()

baseTriangulo = float(input("Ingrese base del triangulo: "))
alturaTriangulo = float(input("ingrese altura del triangulo: "))

areaTriangulo = 0.5 * baseTriangulo * alturaTriangulo
hipotenusaTriangulo = math.sqrt(baseTriangulo**2 + alturaTriangulo**2)
perimetroTriangulo = baseTriangulo + alturaTriangulo + hipotenusaTriangulo

print("El area del triangulo es igual a : ", areaTriangulo)
print("El perimetro del triangulo es igual a: ", perimetroTriangulo)
	

if areaTriangulo >= 3:

	print("El área del triángulo es mayor o igual a 3")
	

