"""
Nombre: CrudListas.py
Objetivo: implementa las funciones crud en una lista en python
Autor: Ricardo Hiram Morales Vaca
Fecha: 4 de agosto de 2020
"""

# Declaramos una lista como variable global
lista = []

def addElement():
    e = input("Ingresa elemento: ")
    lista.append(e)
    print("Elemento agregado exitósamente ...")

    return

def getElement():
    return

def modifyElement():
    return

def delElement():
    return

def printElements():
    for i in lista:
        print("Elemento de la lista: ", i)

def dashboard():
    print("== Operaciones CRUD con Lista en Python ==")
    print("1. Agregar elementos")
    print("2. Buscar elementos")
    print("3. Cambiar elementos")
    print("4. Eliminar elementos")
    print("5. Imprimir elementos")
    print("6. Salir")
    return


def main():
    ciclo = 'S'
    while ciclo == 'S' or ciclo == 's':
        dashboard()
        ciclo = input("Seleccione una opción entre 1 y 5: ")

        if ciclo == 1:
            addElement()
        elif ciclo == 2:    



    else:
        print("*** Fin de programa")


if __name__=="__main__":
    main()
