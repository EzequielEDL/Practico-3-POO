from Inscripcion import Inscripcion

class TallerCapacitacion:
    __idTaller = 0
    __nombre = ''
    __vacantes = 0
    __montoInscripcion = 0
    __inscripciones = None

    def __init__(self, idTaller = 0, nombre = '', vacantes = 0, montoInscripcion = 0):
        self.__idTaller = int(idTaller)
        self.__nombre = str(nombre)
        self.__vacantes = int(vacantes)
        self.__montoInscripcion = float(montoInscripcion)
        self.__inscripciones = []
        
    def __str__(self):
        return ' {}) {} Vacantes: {} Precio: ${}'.format(self.__idTaller, self.__nombre, self.__vacantes, self.__montoInscripcion)

    def getIdTaller(self):
        return self.__idTaller

    def getNombre(self):
        return self.__nombre

    def getVacantes(self):
        return self.__vacantes

    def getMontoInscripcion(self):
        return self.__montoInscripcion
        
    def addInscripcion(self, persona):
        if self.__vacantes > 0 :
            inscripcion = Inscripcion(False, persona, self)
            self.__inscripciones.append(inscripcion)
            self.__vacantes = self.__vacantes - 1
            return inscripcion
            
        else : return None
    
    def getInscripciones(self):
        return self.__inscripciones