"""
Nombre: Punto.py
Objtivo: Herencia
autor: Ricardo Hiram Morales Vaca
Fecha: 30 de julio de 2020
"""
import math
from Punto import Punto

class Circunferencia(Punto):
    #Constructor
    def __init__ (self,valorX, valorY, vradio):
        Punto.__init__(self, valorX, valorY)
        #Atributo de la circunferencia
        self.radio = vradio
    
    def getRadio(self):
        return radio
    
    def setRadio(self, vradio):
        self.radio = vRadio

    def getArea(self):
        return math.pi*math.pow(self.radio, 2)

    def toString(self):
        return Punto.toString(self)+" y el valor del radio es: "+str(self.radio)+" y el área es: "+ str(self.getArea())

