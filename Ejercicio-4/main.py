#|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | Max 19 TABs
#Ejercicio 4
#@author: Ezequiel

import keyboard #module extern: pip3 install keyboard
import os
import colorama
import time
from colorama import Fore, Back
from control_employe import ControlEmploye


#Color Configuration
COLOR_OFF = Fore.GREEN
COLOR_ON = Fore.RED


def option1(control_employe):
    dni = input(' \244 Ingresar DNI: ')
    hours = int(input(' \244 Cantidad de horas trabajadas: '))
    control_employe.set_hours_employe(dni, hours)
    input('\n\n<< press any key to continue >>')

def option2(control_employe):
    task = input(' \244 Ingresar tarea: ')
    control_employe.str_task_amount(task)
    input('\n\n<< press any key to continue >>')

def option3(control_employe):
    print(' \244 Listado de empleados con sueldo menor a $25.000')
    list_employe = control_employe.list_employe_salary(25000)
    print('\n █{:<8}█{:<28}█{:<8}█'.format(' Nombre', ' Direccion', ' DNI'))
    
    for obj in list_employe:
        print(' │{:<8}│{:<28}│{}│'.format(obj.get_name(), obj.get_address(),
            obj.get_dni()))

    input('\n\n<< press any key to continue >>')

def option4(control_employe):
    control_employe.str_salary()
    input('\n\n<< press any key to continue >>')

select = {1: option1, 2: option2, 3: option3, 4: option4}

def menu(opc, control_employe):
    input()
    func = select.get(opc, lambda: print(" * Opcion Incorrecta *"))
    func(control_employe)

def set_color(opc_active, opc_select):
    color = '  ' + COLOR_OFF
    if opc_active == opc_select : color = '  ' + COLOR_ON + ' >'
    return color

if __name__ == "__main__":
    colorama.init()
    colorama.init(autoreset=True)
    os.system('cls')
    size = int(input(' * Cantidad de empleados (TOTAL 30): '))
    control_employe = ControlEmploye(size)
    input('{} * Archivos cargados *'.format(control_employe))

    #Menu Configuration
    opc, MAX = 1, 5
    flag = False

    while not flag:
        os.system('cls')

        print(COLOR_ON + '\n\tMenu Template\n')
        print(set_color(opc, 1) + '  Registrar horas')
        print(set_color(opc, 2) + '  Total de tarea')
        print(set_color(opc, 3) + '  Ayuda')
        print(set_color(opc, 4) + '  Calcular sueldo')
        print(set_color(opc, 5) + '  Salir')

        key = keyboard.read_key()
        print('\n  ' + key)
        if key == 'flecha abajo' and opc < MAX:            
            opc = opc + 1
            time.sleep(0.3)

        if key == 'flecha arriba' and opc > 1:
            opc = opc - 1
            time.sleep(0.3)

        if key == 'enter':
            
            if opc != MAX :
                menu(opc, control_employe)
            else : flag = True
            time.sleep(0.3)

        