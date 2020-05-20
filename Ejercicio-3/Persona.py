
class Persona:
    __nombre = ''
    __direccion = ''
    __dni = ''

    def __init__(self, nombre = '', direccion = '', dni = ''):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni

    def __str__(self):
        return ' Nombre: {} Direccion: {} DNI: {}'.format(self.__nombre, self.__direccion, self.__dni)

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion
    
    def getDni(self):
        return self.__dni