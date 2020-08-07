"""
Nombre: diccionarios.py
Objetivo implementa las funciones crud en un lista en python
Autor: Ricardo Hiram Morales Vaca
Fecha: 5 de Agosto 2020
"""

"""
Un diccionario es una estructura de datos que almacena valores heterogeneos pero los 
almacena en un formato de clave: valor. Quiere decir que cada elemento en el edireccionario
se almacena como una lista de pares key:valor.
Ejemplo 'nombre': Ricardo Hiram Moreles Vaca
No son mutables, significa que no cambian. Una vez que los creamos permanecerán
con los mismos valores, no podremos introducir mas datos
"""

def main():
    #Creamos diccionario con distintos key y datos
    dic = {'clave':20082133, 'nombre':'Erick Jose Verduzco Campos','Edad':22, 'cursos':['Python','Programacion web','Inteligencia Artificial' ]}
    #Listar items del diccionario
    print("Los items son",dic)
    #Imprimir un item de un diccionario proporcionado su key
    print("El elemento de la key es: ", dic['nombre'])
    #Imprimir los valores de los keys del diccionario
    for i in dic:
        print(i," : ",dic[i])

    #EN el caso de la lista incluidad como un item del diccionario, lo accesamos
    print("\n")
    for i in dic['cursos']:
        print(i)

if __name__=="__main__":
    main()