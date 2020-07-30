"""
Nombre: Punto.py
Objtivo: Muestra como llamar desde otro archivo
autor: Ricardo Hiram Morales Vaca
Fecha: 30 de julio de 2020
"""

from Punto import Punto

#creamos objetos dentro del mismo archivo
puntoA = Punto(0,0)
#invocamos los metodos get
print("el valor de la coordenada X es: ", puntoA.getX())
print("el valor de la coordenada X es: ", puntoA.getY())

#invocamos los metodos set
puntoA.setX(23)
puntoA.setY(12)

#imptimimos los valores de lo atributos el objeto puntoA
print(puntoA.toString())

#creamos objetos dentro del mismo archivo
puntoB = Punto(-10,-20)
#Invocamos metodo get
print("el valor de la coordenada X es: ", puntoB.getX())
print("el valor de la coordenada X es: ", puntoB.getY())
#invocamos metodo set    
puntoB.setX(66)
puntoB.setY(99)
#imprimimos los valores de los atributos del objeto puntoA
print(puntoB.toString())