
class Sabor:
    __numero = 0
    __nombre = ''
    __descripcion = ''

    def __init__(self, numero, nombre, descripcion):
        self.__numero = int(numero)
        self.__nombre = str(nombre)
        self.__descripcion = str(descripcion)

    def __str__(self):
        return '{})_{}: {}'.format(self.__numero, self.__nombre, self.__descripcion)

    def getNumero(self):
        return self.__numero

    def getNombre(self):
        return self.__nombre

    def getDescripcion(self):
        return self.__descripcion

    