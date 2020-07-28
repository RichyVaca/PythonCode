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
	if (n2 != 0):
		return n1/n2
	else:
		print ("Error, no se puede dividir entre cero...")

def compara (n1, n2):
	if n1>n2:
		print("El mayor es n1: ",n1, " que ",n2)
	elif n2>n1:
		print("El mayor es: {} que {}".format(n2,n1))
	else:
		print("Los numeros son iguales: {},{}.".format(n1,n2))

#funcion para mostrar operacion  de for
def cuenta(n1, n2):
	if (n2>n1):
		for  i in range(n1, n2+1):
			print("valor de i: {}".format(i))
	elif(n1>n2):
                for  i in range(n1, n2-1, -1):
                        print("valor de i: {}".format(i))
	else:
		print("Los numeros son iguales, no puedo contar: {} , {}".format(n1, n2))
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
		#funcion compara
		compara(a,b)
		cuenta(a,b)

		#preguntamos por otra operación
		ciclo = input("Desea otra operación (S/N)?")
	else:
		print("*** Fin de programa")

if __name__ == "__main__":
	main()
