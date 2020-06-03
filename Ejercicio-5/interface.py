#   72 max spaces
#   Ejercicio 5
#   @author: Ezequiel

from zope.interface import Interface


class IElement(Interface):
#   Insertar Elemento
    def ins_element(element, index):
        pass

#   Agregar Elemento
    def add_element(element):
        pass

#   Mostrar Elemento
    def show_element(index):
        pass
