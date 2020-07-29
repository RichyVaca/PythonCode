"""
Nombre: ventana.py
Objtivo Muestra como trabajar con ventanas gui en python y tkinter
autor: Ricardo Hiram Morales Vaca
"""

#Importar las librerias de tkinter
import tkinter.ttk
from tkinter import*
from tkinter import ttk
#funcion sentToServer():
def sendToServer():
    print("Enviado")


#funcion main

def main():
    #Creamos la ventana contenedora
    win = Tk()
    #Modificamos parametros de la ventana win
    win.geometry("400x400")
    win.title("Mi primer ventana en Python Tkinter")
    #Creamos etiqueta
    label = ttk.Label(win, text="Texto enviar al servidor").pack(side=TOP)
    textCampo = ttk.Entry(win).pack(side=TOP)

    #Creamos un boton para enviar el contenido de la propiedad text del entry al servidor
    ttk.Button(win, text="Enviar mensaje", command=sendToServer).pack(side=BOTTOM)

    #Creamos un boton en la ventana y lo colocamos en la ventana
    ttk.Button(win, text="Cerrar ventana", command=quit).pack(side=BOTTOM)

    #hacemos un ciclo para dibujar y esperar eventos
    win.mainloop()

#Para funcion main
if __name__ == "__main__":
    main()