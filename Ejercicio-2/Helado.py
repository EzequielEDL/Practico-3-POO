from ManejaSabores import ManejaSabores

class Helado:
    __gramos = 0
    __sabores = []

    def __init__(self, gramos, sabores):
        self.__gramos = int(gramos)
        self.__sabores = []
        self.__addSabor(sabores)

    def __str__(self):
        return '{} gr.'.format(self.__gramos)

    def getGramos(self):
        return self.__gramos

    def __addSabor(self, sabores):
        manejaSabor = ManejaSabores()

        for i in range(len(sabores)):
            self.__sabores.append(manejaSabor.getListSabor()[sabores[i] - 1])
    
    def getSabores(self):
        return self.__sabores
