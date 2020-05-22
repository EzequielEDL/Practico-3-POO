from Inscripcion import Inscripcion
import numpy
import csv

class ManejaInscripcion:
    #__dimension = 0
    __arrayInscripcion = None

    def __init__(self, dimension = 0):
        #self.__dimension = dimension
        #self.__arrayInscripcion = numpy.array(Inscripcion)
        self.__arrayInscripcion = []
    
    def __str__(self):
        c = ''
        for i in range(len(self.__arrayInscripcion)) :
            c = c + str(self.__arrayInscripcion[i]) + '\n'
        
        return c

    def addArrayInscripcion(self, inscripcion):
        self.__arrayInscripcion.append(inscripcion)
        self.__dimension = len(self.__arrayInscripcion)

    def getArrayInscripcion(self):
        return self.__arrayInscripcion

    def consultarInscripcion(self, dni):
        i = 0
        while i < len(self.__arrayInscripcion) and self.__arrayInscripcion[i].getPersona().getDni() != dni :
            i = i + 1

        if i < len(self.__arrayInscripcion) :
            print('\n Nombre: {}'.format(self.__arrayInscripcion[i].getTaller().getNombre()))
            if self.__arrayInscripcion[i].getPago() : print(' No adeuda ningun monto')
            else:print(' Adeuda: {}'.format(self.__arrayInscripcion[i].getTaller().getMontoInscripcion()))
            print(self.__arrayInscripcion[i])

    def pagoInscripcion(self, dni):
        i = 0
        while i < len(self.__arrayInscripcion) and self.__arrayInscripcion[i].getPersona().getDni() != dni :
            i = i + 1
        
        if i < len(self.__arrayInscripcion) :
            self.__arrayInscripcion[i].setPago(True)
            print(self.__arrayInscripcion[i])
    
    def saveFile(self):
        #dni, idTaller, fecha y pago.
        file = open("inscripciones.csv",'w')

        # Write data to file
        for i in range(len(self.__arrayInscripcion)):
            dni = self.__arrayInscripcion[i].getPersona().getDni()
            idTaller = self.__arrayInscripcion[i].getTaller().getIdTaller()
            fecha = self.__arrayInscripcion[i].getFecha()
            pago = self.__arrayInscripcion[i].getPago()
            
            file.write(str(dni) + ',' + str(idTaller) + ',' + str(fecha) + ',' + str(pago))
            file.write('\n')

        file.close()
        print(' * Archivo generado ! inscripciones.csv')
        