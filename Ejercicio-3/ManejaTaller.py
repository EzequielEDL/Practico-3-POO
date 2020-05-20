from TallerCapacitacion import TallerCapacitacion

import numpy as np
import csv

class ManejaTaller:
    __dimension = 0
    __arrayTaller = None
    
    def __init__(self):
        file = open('talleres.csv')
        reader = csv.reader(file, delimiter = ',')
        i = 0
        self.__dimension = int(next(reader)[0])
        self.__arrayTaller = np.empty(self.__dimension, dtype = TallerCapacitacion)

        for row in reader:
            tallerCapacitacion = TallerCapacitacion(row[0], row[1], row[2], row[3])
            self.__arrayTaller[i] = tallerCapacitacion
            i = i + 1

        file.close()

    def __str__(self):
        c = ''
        for i in range(self.__dimension) :
            c = c + str(self.__arrayTaller[i]) + '\n'
        
        return '\n' + c

    def getArrayTaller(self):
        return self.__arrayTaller
    
    def inscribirPersona(self, persona, idTaller):
        return self.__arrayTaller[idTaller - 1].addInscripcion(persona)
    
    def consultarInscripciones(self, idTaller):
        for i in range(len(self.__arrayTaller[idTaller - 1].getInscripciones())) :
            print(self.__arrayTaller[idTaller - 1].getInscripciones()[i].getPersona())
