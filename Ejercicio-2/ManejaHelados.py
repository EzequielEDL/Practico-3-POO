from Helado import Helado
from ManejaSabores import ManejaSabores

class ManejaHelados:
    __listVentas = []
    __manejaSabores = None
    __countSabores = []

    def __init__(self):
        self.__listVentas = []
        self.__manejaSabores = ManejaSabores()
        self.__countSabores = []
        self.__cereoCountSabores()

        for i in range(len(self.__manejaSabores.getListSabor())):
            self.__countSabores.append([self.__manejaSabores.getListSabor()[i].getNumero(), 0])

    def addListVentas(self, helado):
        self.__listVentas.append(helado)

    def __cereoCountSabores(self):
        for i in range(len(self.__countSabores)):
            self.__countSabores[i][1] = 0

    def __orderCountSabores(self):
        for i in range(len(self.__countSabores)): #ordenar por mayor
            j = i + 1
            for j in range(len(self.__countSabores)):
                if self.__countSabores[i][1] > self.__countSabores[j][1] :
                    auxCountSabores = self.__countSabores[i]
                    self.__countSabores[i] = self.__countSabores[j]
                    self.__countSabores[j] = auxCountSabores

    def regVenta(self):
        gramos = int(input(' Tipo de Helado (100gr, 150gr, 250gr, 500gr y 1000gr): '))
        sabores = []

        if gramos == 100 or  gramos == 150 or  gramos == 500 or  gramos == 1000 :

            print(' Sabores (MAX 4) - Finalizar con 0\n')
            sabor = int(input(' Sabor: '))

            while len(sabores) < 4 and sabor != 0:
                sabores.append(sabor - 1)
                if len(sabores) < 4 : sabor = int(input(' Sabor: '))
            
            print('\n - Venta Realizada -')
            helado = Helado(gramos, sabores)
            self.__listVentas.append(helado)

        else :
            print('\nERROR - Tipo de Helado Incorrecto')

    def showSaboresPedidos(self, max):
        self.__cereoCountSabores()

        for i in range(len(self.__manejaSabores.getListSabor())): #recorrer los sabores
            for j in range(len(self.__listVentas)): #recorrer ventas de helados
                for k in range(len(self.__listVentas[j].getSabores())): #recorrer sabores de cada helado vendido
                    if self.__countSabores[i][0] == self.__listVentas[j].getSabores()[k].getNumero() :
                        self.__countSabores[i][1] = self.__countSabores[i][1] + 1 #contador de cada sabor 
        
        self.__orderCountSabores()

        if max <= len(self.__countSabores) :
            for i in range(max - 1) :
                print('Pedidos: {} - Sabor: {}'.format(self.__countSabores[i][1], self.__manejaSabores.getListSabor()[self.__countSabores[i][0] - 1]))

    def showHeladosTipos(self, tipoHelado):
        numSabores = []
        
        for j in range(len(self.__listVentas)): #recorrer ventas de helados
            
            if tipoHelado == self.__listVentas[j].getGramos() :
                for k in range(len(self.__listVentas[j].getSabores())):
                    if not self.__listVentas[j].getSabores()[k].getNumero() in numSabores :
                        numSabores.append(self.__listVentas[j].getSabores()[k].getNumero())
        
        for i in range(len(numSabores)):
            print(' {}'.format(self.__manejaSabores.getListSabor()[numSabores[i] - 1]))

    def getSaboresGramos(self, numSabor):
        acumGram = 0

        for j in range(len(self.__listVentas)): #recorrer ventas de helados
            for k in range(len(self.__listVentas[j].getSabores())): #recorrer sabores de cada helado vendido
                #print('{} == {}'.format(numSabor, self.__listVentas[j].getSabores()[k].getNumero())) 
                if numSabor == self.__listVentas[j].getSabores()[k].getNumero() :
                    acumGram = acumGram + self.__listVentas[j].getGramos() / len(self.__listVentas[j].getSabores())
                    #print('{} = {} + {} / {}'.format(acumGram, acumGram, self.__listVentas[j].getGramos(), len(self.__listVentas[j].getSabores())))

        return acumGram
    
