#|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Max 19 TABs
#   subclass DePlanta
#   __dni, __name, __address, __phone
#   __basic_salary, __antiquity

from employe import Employe


class Plant(Employe):
    __basic_salary = 0
    __antiquity = 0
    __salary = 0

    def __init__(self, dni, name, address, phone, basic_salary, antiquity):
        super().__init__(dni, name, address, phone)
        self.__basic_salary = float(basic_salary)
        self.__antiquity = int(antiquity)
        self.__salary = self.__basic_salary + (self.__basic_salary * 0.01) * self.__antiquity

    def __str__(self):
        return super().__str__() + '{}║{:<2}║{:<6}║'.format(self.__basic_salary,
            self.__antiquity, self.__salary)

#   instance method

#   setters & getters

    def get_basic_salary(self):
        return self.__basic_salary

    def get_antiquity(self):
        return self.__antiquity

    def get_salary(self):
        return self.__salary

    def set_basic_salary(self, basic_salary):
        self.__basic_salary = basic_salary
        self.__set_salary()

    def set_antiquity(self, antiquity):
        self.__antiquity = antiquity
        self.__set_salary()

    def __set_salary(self):
        self.__salary = self.__basic_salary + (self.__basic_salary * 0.01) * self.__antiquity
