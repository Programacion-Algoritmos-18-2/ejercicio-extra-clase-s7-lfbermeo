class OrdenamientoSeleccion(object):
    def __init__(self, datos):
        self.datos = datos
	#Con este metodo realiza el ordenamiento de los valores
    def ordenar(self):
        masPequenio = 0

        for i in range(len(self.datos)-1):
            masPequenio = i
            for indice in range(i+1, len(self.datos)):
                if (self.datos[indice] < self.datos[masPequenio]):
                    masPequenio = indice
            self.intercambiar(i, masPequenio)
            print(self.__str__())

	#Con este método realizo el intercambio de elementos con la varieble temporal
    def intercambiar(self, primero, segundo):
        temporal = self.datos[primero]
        self.datos[primero] = self.datos[segundo]
        self.datos[segundo] = temporal

	#Método str para realizar la impresión 
    def __str__(self):
        temporal = ""
        for elemento in self.datos:
            temporal += " {} ".format(elemento)
        temporal += "\n"
        return temporal
