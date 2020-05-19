from Sabor import Sabor
import csv

class ManejaSabores:
    __listSabor = []

    def __init__(self):

        self.__listSabor = []
        
        file = open('sabores.csv')
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            sabor = Sabor(row[0], row[1], row[2])
            self.__listSabor.append(sabor)
        
        file.close()

    def __str__(self):
        str1 = '\n - Lista de Sabores -\n'
        for i in range(len(self.__listSabor)):
            str1 = str1 + ' ' + str(self.__listSabor[i]) + '\n'

        return str1

    def getListSabor(self):
        return self.__listSabor
