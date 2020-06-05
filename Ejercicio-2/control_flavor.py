#	Clase Manejador de sabor

from flavor import Flavor
import csv


class ControlFlavor:
    __list_flavor = []

    def __init__(self):
        self.__list_flavor = []
        
        file = open('flavors.csv')
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            flavor = Flavor(row[0], row[1], row[2])
            self.__list_flavor.append(flavor)
        
        file.close()

    def __str__(self):
        str1 = '\n - Lista de Sabores -\n'
        for i in range(len(self.__list_flavor)):
            str1 = str1 + ' ' + str(self.__list_flavor[i]) + '\n'

        return str1

    def __len__(self):
        return len(self.__list_flavor)
        
#   Instance methods

    def get_list_flavor(self):
        return self.__list_flavor

