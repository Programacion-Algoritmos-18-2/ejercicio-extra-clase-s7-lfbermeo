from paquete.OrdenamientoSeleccion import OrdenamientoSeleccion
#Le asigno valores a mi arreglo
valores = [4, 3, 1, 9, 8, 7]
#Creó un objeto para enviar los valores
arregloOrden = OrdenamientoSeleccion(valores)
print("Arreglo desordenado")
print(arregloOrden)
#Instancio mi objeto y llamo al método ordenar
arregloOrden.ordenar()
#imprimo
print(arregloOrden)
