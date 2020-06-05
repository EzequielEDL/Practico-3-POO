#   class Empleado
#   __dni, __name, __address, __phone

import abc
from abc import ABC


class Employe:
    __dni = ''
    __name = ''
    __address = ''
    __phone = ''

    def __init__(self, dni, name, address, phone):
        self.__dni = dni
        self.__name = name
        self.__address = address
        self.__phone = phone

    def __str__(self):
        return '║{}║{:<8}║{:<28}║{:<7}║{:<8}║'.format(self.__dni, self.__name,
            self.__address, self.__phone, self.get_salary())

#   instance method

#   setters & getters

    def get_dni(self):
        return self.__dni

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone
    
    def set_dni(self, dni):
        self.__dni = dni
    
    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address
    
    def set_phone(self, phone):
        self.__phone = phone

    @abc.abstractmethod
    def get_salary():
        pass