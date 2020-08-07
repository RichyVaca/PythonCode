"""
Nombre: Circunferencia
Objetivo: Permite calcular el area de una circunferencia
Autor: Ricardo Hiram Morales Vaca
Fecha: 28 de julio de 2020
"""

#importamos libreria math
import math

#---------------------------
#funcion para calcular area
#---------------------------

def calcularArea(valorRadio):
	return math.pi*math.pow(valorRadio, 2)



#Modulo principal
def main():
	ciclo = 'S'
	while (ciclo == 's' or ciclo == 'S'):
		print("--- Programa para caluclar area de circunferencia ---")
		vradio = int(input("Introduce valor del radio"))
		print("El area de la circunferencia  con radio igual a: {}, es: {}".format(vradio, calcularArea(vradio)))
		ciclo = input("otro calculo (s/n)?")
	else:
		print("fin del programa")
if __name__ == "__main__":
	main()
