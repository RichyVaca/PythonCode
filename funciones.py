


"""
Nombre: funciones.py
Objetivo: Muestra la operacion de las funciones en python
autor: Ricardo Hiram Morales Vaca
fecha: 27 julio de 2020
"""

def mensaje():
	print("saludo desde mensaje")

def regresaMensaje():
	return "saludo desde regresaMensaje"

def printMensaje(msg):
	return print(msg)

def suma(n1, n2):
	return n1+n2

def resta (n1, n2):
	return n1-2

def multiplicacion(n1, n2):
	return n1*n2

def division (n1, n2):
	return n1/n2

def main():
	ciclo = 's'
	while ciclo == 's' or ciclo == 'S':
		#invocamos función mensaje
		mensaje()
		#invocamos función regresaMensaje
		regresaMensaje()
		#invocamos funcion  printMensaje
		printMensaje("hola te saludo...")
		#invocamos la funcion suma, resta, multiplicacion y division
		a = int(input("Ingresar numero "))
		b = int(input("ingresar otro numero "))
		print("La suma de es igual a ", suma(a,b))
		print("La resta de es igual a ", resta(a,b))
		print("La multiplicacion de es igual a ", multiplicacion(a,b))
		print("La division de es igual a ", division(a,b))

		#preguntamos por otra operación
		ciclo = input("Desea otra operación (S/N)?")
	else:
		print("*** Fin de programa")

if __name__ == "__main__":
	main()

