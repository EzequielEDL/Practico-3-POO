#|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Max 19 TABs
#   subclase Externos
#   __dni, __name, __address, __phone
#   __task, __date_start, __date_end, __amount_viatic, __amount_secure, __work_price

from datetime import datetime
from employe import Employe


class External(Employe):
    __task = ''
    __date_start = None
    __date_end = None
    __amount_viatic = 0
    __amount_secure = 0
    __work_price = 0
    __salary = 0

    def __init__(self, dni, name, address, phone, task, date_start, date_end,
            amount_viatic, amount_secure, work_price):
        super().__init__(dni, name, address, phone)
        self.__task = task
        self.__date_start = datetime.strptime(date_start, '%d/%m/%Y')
        self.__date_end = datetime.strptime(date_end, '%d/%m/%Y')
        self.__amount_viatic = float(amount_viatic)
        self.__amount_secure = float(amount_secure)
        self.__work_price = float(work_price)
        self.__salary = self.__work_price - self.__amount_secure - self.__amount_viatic

    def __str__(self):
        return super().__str__() + '{:<12}║{}║{}║{:<6}║{:<6}║{:<7}║{:<7}║'.format(self.__task,
            self.__date_start.date(), self.__date_end.date(), self.__amount_viatic,
            self.__amount_secure, self.__work_price, self.__salary)

#   instance method

#   setters & getters

    def get_task(self):
        return self.__task

    def get_date_start(self):
        return self.__date_start
    
    def get_date_end(self):
        return self.__date_end

    def get_amount_viatic(self):
        return self.__amount_viatic
    
    def get_amount_secure(self):
        return self.__amount_secure
    
    def get_work_price(self):
        return self.__work_price

    def get_salary(self):
        return self.__salary
    
    def set_task(self, task):
        self.__task = task
    
    def set_date_start(self, date_start):
        self.__date_start = date_start
    
    def set_date_end(self, date_end):
        self.__date_end = date_end
    
    def set_amount_viatic(self, amount_viatic):
        self.__amount_viatic = amount_viatic
        self.__set_salary()

    def set_amount_secure(self, amount_secure):
        self.__amount_secure = amount_secure
        self.__set_salary()

    def set_work_price(self, work_price):
        self.__work_price = work_price
        self.__set_salary()

    def __set_salary(self):
        self.__salary = self.__work_price - self.__amount_secure - self.__amount_viatic
