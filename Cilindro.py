"""
Nombre: Punto.py
Objtivo: Herencia
autor: Ricardo Hiram Morales Vaca
Fecha: 30 de julio de 2020
"""
from Circunferencia import Circunferencia

class Cilindro(Circunferencia):
    #Definimos constructor
    def __init__(self, valorX, valorY, valorRadio, valorAltura):
        #constructor de circunferencia
        Circunferencia.__init__(self, valorX, valorY, valorRadio)
        #constructor de cilindro
        self.altura = valorAltura

    def getAltura(self):
        return self.altura
    def setAltura(self, valorAltura):
        self.altura = valorAltura

    def toString(self):
        return Circunferencia.toString(self)+" y la altura es :"+str(self.altura)+" el volumen es: "+str(self.getVolumen())
    def getVolumen(self):
        return Circunferencia.getArea(self) * self.getAltura()

c = Cilindro(2,3,4,7)
print(c.toString())