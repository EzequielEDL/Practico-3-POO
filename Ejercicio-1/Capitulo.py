
class Capitulo:
    __titulo = ''
    __cantidadPaginas = 0

    def __init__(self, titulo = '', cantidadPaginas = 0):
        self.__titulo = str(titulo)
        self.__cantidadPaginas = int(cantidadPaginas)

    def __str__(self):
        return '{}, {}'.format(self.__titulo, self.__cantidadPaginas)

    def getCantidadPaginas(self):
        return self.__cantidadPaginas

    def getTitulo(self):
        return self.__titulo