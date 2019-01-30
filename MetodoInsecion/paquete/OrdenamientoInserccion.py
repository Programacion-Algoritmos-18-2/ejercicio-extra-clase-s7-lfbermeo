class OrdenamientoInsercion(object):
    def __init__(self, datos):
        self.datos = datos
    #Creo la función que va ordenando los valores
    def ordenar(self):
        insercion = 0

        for siguiente in range(1, len(self.datos)):
            insercion = self.datos[siguiente]
            moveElemento = siguiente
            while (moveElemento > 0 and self.datos [moveElemento-1] > insercion):
                self.datos [moveElemento] =  self.datos [moveElemento -1 ]
                moveElemento-=1
            self.datos[moveElemento] = insercion    
            print(self.__str__())    

    #Está función nos sirve para saber como se va ordenando uno por uno imprimiendola
    def impirmirPasada(self, pasada, indice):
        print("Despues de pasada {}: ".format(pasada))
        for i in range(indice):
            print(self.datos[i]+" ")
        print(self.datos[indice]+"* ")

        for i in (indice+1, len(self.datos)):
            print(self.datos[i]+" ")
        
        for i in (pasada+1):
            print("---------------")
    
    #Impresión
    def __str__(self):
        temporal = ""
        for elemento in self.datos:
            temporal += " {} ".format(elemento)
        temporal += "\n"
        return temporal

                   