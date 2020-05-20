import time

class Inscripcion:
    __fecha = None
    __pago = False
    __persona = None
    __tallerCapacitacion = None

    def __init__(self, pago, persona, tallerCapacitacion):
        self.__fecha = time.strftime("%d/%m/%y")
        self.__pago = pago
        self.__persona = persona
        self.__tallerCapacitacion = tallerCapacitacion

    def __str__(self):
        wup = ' ┌{:─<20}┐\n'.format('─')
        wdn = ' └{:─<20}┘'.format('─')
        c0 = ' {0:<6}{1:<15}{0}\n'.format('│', 'INSCRIPCION')
        c1 = ' {0}{1}{2:<13}\n'.format('│', 'Fecha: ', self.__fecha)
        if self.__pago : paystr = 'Realizado'
        else : paystr = 'Pendiente'
        c2 = ' {0}{1}{2:<15}\n'.format('│', 'Pago: ', paystr)

        return wup + c0 + c1 + c2 + wdn

    def getFecha(self):
        return self.__fecha
    
    def getPago(self):
        return self.__pago

    def getInscripcion(self):
        return self.__persona

    def getTallerCapacitacion(self):
        return self.__tallerCapacitacion

    def getPersona(self):
        return self.__persona

    def getTaller(self):
        return self.__tallerCapacitacion
    
    def setPago(self, pago):
        self.__pago = pago