#   class Maneja Empleados
#   __

from employe import Employe
from external import External
from hired import Hired
from plant import Plant
from datetime import datetime
import numpy as np
import csv

from interface import ITreasurer, IManager
import zope


@zope.interface.implementer(ITreasurer)
@zope.interface.implementer(IManager)
class ControlEmploye:
    __dimension = 0
    __array_employe = None

    def __init__(self, dimension):
        self.__dimension = dimension
        self.__array_employe = np.empty(self.__dimension, dtype = Employe)
        self.__load_file('external')
        self.__load_file('hired')
        self.__load_file('plant')

    def __str__(self):
        c = ''

        for i in range(len(self.__array_employe)) :
            index = '{:>02}-'.format(i + 1)
            c = c + index + str(self.__array_employe[i]) + '\n'
        
        return c

    def __load_file(self, name_file):
        file = open(name_file + '.csv')
        reader = csv.reader(file, delimiter = ',')

        i = sum(x is not None for x in self.__array_employe)

        for row in reader:
            if i < self.__dimension:
                if name_file == 'external':
                    employe = External(row[0], row[1], row[2], row[3], row[4],
                        row[5], row[6], row[7], row[8], row[9])

                elif name_file == 'hired':
                    employe = Hired(row[0], row[1], row[2], row[3], row[4],
                        row[5], row[6])

                elif name_file == 'plant':
                    employe = Plant(row[0], row[1], row[2], row[3], row[4],
                        row[5])

                self.__array_employe[i] = employe
                i = i + 1

        file.close()

    def set_hours_employe(self, dni, hours):
        i = 0

        while i < self.__dimension and self.__array_employe[i].get_dni() != dni:
            i = i + 1
        
        if i < self.__dimension:
            if isinstance(self.__array_employe[i], Hired):
                print('\n * Horas: {}'.format(self.__array_employe[i].get_hours()))
                hours = hours + self.__array_employe[i].get_hours()
                self.__array_employe[i].set_hours(hours)
                print('\n * Horas actualizadas: {}'.format(self.__array_employe[i].get_hours()))
            
            else : print('\n * Empleado Contratado : Inexistente')

        else : print('\n * DNI : Inexistente')

    def str_task_amount(self, task):
        total_amount = 0
        print('\n * Fechas\n █{:<11}█{:<11}█'.format(' Fin', ' Actual'))

        for obj in self.__array_employe:
            if isinstance(obj, External):
                if obj.get_task() == task:
                    print(' │{} │ {}│'.format(obj.get_date_end().date(),
                        datetime.now().date()))
                    if obj.get_date_end() < datetime.now():
                        total_amount = total_amount + obj.get_salary()
        
        if total_amount != 0:
            print('\n * Monto total a pagar: {}'.format(total_amount))

        else:
            print('\n * No hay ninguna tarea en progreso')

    def list_employe_salary(self, max_salary):
        list_employe = []
            
        for obj in self.__array_employe:
            if obj.get_salary() < max_salary:
                list_employe.append(obj)

        return list_employe

    def str_salary(self):
        print('\n █{:<8}█{:<16}█{:<8}█'.format(' Nombre', ' Telefono', ' Sueldo'))
        acum_salary = 0

        for obj in self.__array_employe:
            print(' │{:<8}│{:<16}│{:<8}│'.format(obj.get_name(), obj.get_phone(), 
                obj.get_salary()))
            acum_salary = acum_salary + obj.get_salary()
        
        print('\n * Monto total de los salarios:', acum_salary)

#   Interface methods

    def __search_dni(self, dni):
        i = 0
        while i < self.__dimension and self.__array_employe[i].get_dni() != dni:
            i += 1

        if i < self.__dimension:
            return i
        else:
            return -1

    def show_salary(self, dni):
        i =  self.__search_dni(dni)
        
        if i != -1:
            print('\n\t    Gastos: {}'.format(self.__array_employe[i].get_salary()))

    def mod_salary_basic(self, dni, salary_basic):
        i =  self.__search_dni(dni)
        
        if i != -1:
            self.__array_employe[i].set_salary_basic(salary_basic)
            print('\n * Modificacion realizada !')

    def mod_amount_viatic(self, dni, amount_viatic):
        i =  self.__search_dni(dni)
        
        if i != -1:
            self.__array_employe[i].set_amount_viatic(amount_viatic)
            print('\n * Modificacion realizada !')

    def mod_hour_price(self, hour_price):
        Hired.set_hour_price(hour_price)
        print('\n * Modificacion realizada !')