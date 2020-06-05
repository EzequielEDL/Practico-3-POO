#   subclase Contratados
#   __dni, __name, __address, __phone
#   __date_start, __date_end, __hours, __salary, hour_price

from datetime import datetime
from employe import Employe


class Hired(Employe):
    __date_start = None
    __date_end = None
    __hours = 0
    hour_price = 300.0

    def __init__(self, dni, name, address, phone, date_start, date_end, hours):
        super().__init__(dni, name, address, phone)
        self.__date_start = datetime.strptime(date_start, '%d/%m/%Y')
        self.__date_end = datetime.strptime(date_end, '%d/%m/%Y')
        self.__hours = int(hours)

    def __str__(self):
        return super().__str__() + '{}║{}║{:>02}║{}║'.format(self.__date_start.date(),
               self.__date_end.date(), self.__hours, self.hour_price)

#   instance method

#   setters & getters

    def get_date_start(self):
        return self.__date_start

    def get_date_end(self):
        return self.__date_end
    
    def get_hours(self):
        return self.__hours

    def get_salary(self):
        return self.__hours * self.hour_price
    
    def set_date_start(self, date_start):
        self.__date_start = date_start

    def set_date_end(self, date_end):
        self.__date_end = date_end

    def set_hours(self, hours):
        self.__hours = hours

    #   class method
    #   setters & getters
    
    @classmethod
    def get_hour_price(cls):
        return cls.hour_price

    @classmethod
    def set_hour_price(cls, hour_price):
        cls.hour_price = hour_price
