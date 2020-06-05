#   72 max spaces
#   Interface

from zope.interface import Interface


class IElement(Interface):
#   Insertar Elemento
    def insert(element, index):
        pass

#   Agregar Elemento
    def add_end(element):
        pass

    def add_beg(element):
        pass

#   Mostrar Elemento
    def get(index):
        pass
