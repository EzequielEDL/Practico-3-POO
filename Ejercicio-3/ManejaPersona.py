from Persona import Persona

class ManejaPersona:
    __listPersona = []

    def __init__(self):
        self.__listPersona = []
    
    def __str__(self):
        c = ''
        for i in range(len(self.__listPersona)) :
            c = c + str(self.__listPersona[i]) + '\n'
        
        return c

    def getListPersona(self):
        return self.__listPersona

    def addListPersona(self, persona):
        self.__listPersona.append(persona)
