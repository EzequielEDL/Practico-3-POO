from Capitulo import Capitulo

class Libro:
    __idLibro = 0
    __titulo = ''
    __autor = ''
    __editorial = ''
    __isbn = 0
    __cantidadCapitulos = 0
    __listCapitulo = []

    def __init__(self, idLibro = 0, titulo = '', autor = '', editorial = '', isbn = 0, cantidadCapitulos = 0):
        self.__idLibro = int(idLibro)
        self.__titulo = str(titulo)
        self.__autor = str(autor)
        self.__editorial = str(editorial)
        self.__isbn = int(isbn)
        self.__cantidadCapitulos = int(cantidadCapitulos)
        self.__listCapitulo = []

    def __str__(self):
        str1 = '\n{}, {}, {}, {}, {}, {}'.format(self.__idLibro, self.__titulo, self.__autor, self.__editorial, self.__isbn, self.__cantidadCapitulos)
        return str1

    def getCantidadCapitulos(self):
        return self.__cantidadCapitulos

    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
    def addCapitulo(self, titulo, cantidadPaginas):
        capitulo = Capitulo(titulo, cantidadPaginas)
        self.__listCapitulo.append(capitulo)
    
    def getCapitulo(self, index):
        return self.__listCapitulo[index]

    def getCapituloTitulo(self, index):
        return self.__listCapitulo[index].getTitulo()

    def getCantidadPaginas(self):
        pages = 0

        for i in range(self.__cantidadCapitulos):
            pages = pages + self.__listCapitulo[i].getCantidadPaginas()
        
        return pages
    