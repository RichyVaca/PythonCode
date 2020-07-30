"""
Nombre: Punto.py
Objtivo: Muestra como trabajar con objetos
autor: Ricardo Hiram Morales Vaca
Fecha: 30 de julio de 2020
"""

class Punto():
    #definir un constructor
    def __init__(self, valorX, valorY):
        #definimos el nombre de los atributos del objeto
        self.x = valorX
        self.y = valorY

    #lista de metodos get y set
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self, valorX):
        self.x = valorX
    def setY(self, valorY):
        self.y = valorY

    #metodo toString: refresa lo valores de los atributos: x,y
    def toString(self):
        return "Las coordenadas X,Y del punto son:["+ str(self.getX())+","+str(self.getY())+"]"

    
