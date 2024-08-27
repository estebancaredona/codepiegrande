# @autor: Esteban Marin Cardona
# @fecha: 18/08/2024
# @descripcion: Programa en Python muestra un mensaje de acuerdo con la circunferencia de un astro esferico con respecto al sol. se solicita el radio del astro por teclado. el mensaje se mostrara solamente si la circunferencia del astro es mayor que la circunferencia del sol	

import math

radioAstro = float(input("ingrese el radio del astro: "))

circunferenciaAstro = 2 * math.pi * radioAstro 

radioSol = 696340

circunferenciaSol = 2 * math.pi * radioSol

if circunferenciaAstro > circunferenciaSol:
	print(f""" 
		 Circunferencia del Astro: {circunferenciaAstro}
		 El astro tiene una circunferencia mayor que 
		 la circunferencia del sol: {circunferenciaSol}""")