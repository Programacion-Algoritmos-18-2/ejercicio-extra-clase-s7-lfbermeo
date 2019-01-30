from paquete.OrdenamientoInserccion import OrdenamientoInsercion
#Le asigno valores a mi arreglo
valores = [10, 90, 1, 20, 4, 7, 89, 17, 76, 3, 2]
#Creó un objeto para enviar los valores
arregloOrden = OrdenamientoInsercion(valores)
print("Arreglo desordenado")
print(arregloOrden)
#Instancio mi objeto y llamo al método ordenar
arregloOrden.ordenar()
#imprimo
print("Arreglo ordenado")
print(arregloOrden)