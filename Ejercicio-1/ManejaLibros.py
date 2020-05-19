from Libro import Libro
import csv

class ManejaLibros:
    __listLibro = []

    def __init__(self, nameFile = ''):

        file = open(nameFile)
        reader = csv.reader(file, delimiter = ',')
        i = -1

        for row in reader :
            if row[0].isdecimal() :
                libro = Libro(row[0], row[1], row[2], row[3], row[4], row[5])
                self.__listLibro.append(libro)
                i = i + 1

            if not row[0].isdecimal() :
                self.__listLibro[i].addCapitulo(row[0], row[1])
            
        file.close()

    def __str__(self):
        return '{}'.format(self.__listLibro)

    def showLibro(self, id):
        print(' Titulo: {}'.format(self.__listLibro[id].getTitulo()), end = ' ')
        print(' Autor: {}'.format(self.__listLibro[id].getAutor()), end = ' ')
        print(' Paginas: {}'.format(self.__listLibro[id].getCantidadPaginas()))
        print(' Capitulos:')

        for i in range(self.__listLibro[id].getCantidadCapitulos()) :
            print(' {}'.format(self.__listLibro[id].getCapituloTitulo(i)))
    
    def showAutor(self, word):
        for i in range(len(self.__listLibro)) :
            if word in self.__listLibro[i].getTitulo().lower() :
                print('\n Libro: {}\n Autor: {}'.format(self.__listLibro[i].getTitulo(), self.__listLibro[i].getAutor()))

            else :
                for j in range(self.__listLibro[i].getCantidadCapitulos()) :
                    if word in self.__listLibro[i].getCapituloTitulo(j).lower() :
                        print('\n Capitulo: {}\n Autor: {}'.format(self.__listLibro[i].getCapituloTitulo(j), self.__listLibro[i].getAutor()))
            
        