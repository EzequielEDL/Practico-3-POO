#   72 max spaces
#   Program Template
#   @author: Ezequiel

import keyboard #module extern: pip3 install keyboard
import os
import colorama
import time
from colorama import Fore, Back
import csv

from object_encoder import ObjectEncoder
from control_vehicle import ControlVehicle
from vehicle_new import VehicleNew
from vehicle_old import VehicleOld


#Color Configuration
COLOR_OFF = Fore.GREEN
COLOR_ON = Fore.RED

def print_list(list_vehicle):
    j = 0
    print(' ┌{:─<94}┐'.format('─'))
    print(' │{:<2} ■ {:<8} ■ {} ■ {:<8} ■ {:<9} ■ {:<51}│'.format(
        'I', 'Modelo', 'P', 'Color', 'B. Precio', 'Precio'))

    for i in list_vehicle:
        st = str(i)
        print(' │{:<2}{:<92}│'.format(j + 1, st))
        j += 1

    print(' └{:─<94}┘'.format('─'))
    print('\n * CANTIDAD DE VEHICULOS: {} \n'.format(
        len(list_vehicle)))

def option1(control):
    print_list(control.get_list_vehicle())
    index = int(input(' \244 Posicion: '))
    control.insert_vehicle(index - 1 )

    input('\n\n<< press any key to continue >>')

def option2(control):
    print_list(control.get_list_vehicle())
    position = input('\n \244 Al Final o Inicio: ')
    control.add_vehicle(position)

    input('\n\n<< press any key to continue >>')

def option3(control):
    index = int(input(' \244 Posicion: '))
    type_vehicle = control.get_list_vehicle().get(index - 1)

    print(type(type_vehicle))

    input('\n\n<< press any key to continue >>')

def option4(control):
    patent = input('\n \244 Patente: ')
    price_base = float(input('\n \244 Nuevo precio base: '))
    vehicle = control.search_vehicle(patent)
    print('\n * Nuevo precio del vehiculo: {}'.format(vehicle.get_price()))

    input('\n\n<< press any key to continue >>')

def option5(control):
    list_vehicle = control.list_cheap_vehicle()
    print_list(list_vehicle)

    input('\n\n<< press any key to continue >>')

def option6(control):
    print_list(control.get_list_vehicle())

    input('\n\n<< press any key to continue >>')

def option7(control):
    dic = control.toJSON()
    obj = ObjectEncoder()
    obj.save(dic, 'vehicles.json')
    print('\n * Datos almacenados !')

    input('\n\n<< press any key to continue >>')

#   Carga de un archivo CSV
"""
def load_file_csv(control):
    file = open('vehicles.csv')
    reader = csv.reader(file, delimiter = ',')

    for row in reader:
        if len(row) <= 5:
            vehicle = VehicleNew(*row)
        else:
            vehicle = VehicleOld(*row)

        control.get_list_vehicle().add_end(vehicle)

    file.close()"""

select = {1: option1, 2: option2, 3: option3, 4: option4, 5: option5,
    6: option6, 7: option7}

def menu(opc, control):
    input()
    func = select.get(opc, lambda: print(" * Opcion Incorrecta *"))
    func(control)

def set_color(opc_active, opc_select):
    color = '  ' + COLOR_OFF
    if opc_active == opc_select : color = '  ' + COLOR_ON + ' >'
    return color

def main(control):
    #Menu Configuration
    opc, max_opc = 1, 8
    flag = False

    while not flag:
        os.system('cls')
        print(COLOR_ON + '\n\tTuAuto.com\n')
        print(set_color(opc, 1) + '  Insertar un vehículo')
        print(set_color(opc, 2) + '  Agregar un vehículo ')
        print(set_color(opc, 3) + '  Mostrar tipo de Objeto')
        print(set_color(opc, 4) + '  Modificar precio base')
        print(set_color(opc, 5) + '  Vehiculos mas baratos')
        print(set_color(opc, 6) + '  Mostrar todos los vehículos')
        print(set_color(opc, 7) + '  Almacenar')
        print(set_color(opc, 8) + '  Salir')

        key = keyboard.read_key()
        print('\n  ' + key)

        if key == 'flecha abajo' and opc < max_opc:         
            opc = opc + 1
            time.sleep(0.1)

        if key == 'flecha arriba' and opc > 1:
            opc = opc - 1
            time.sleep(0.1)

        if key == 'enter':
            if opc != max_opc :
                menu(opc, control)

            else : flag = True
            time.sleep(0.1)

if __name__ == "__main__":
    colorama.init()
    colorama.init(autoreset=True)
    
    obj = ObjectEncoder()
    control = obj.Decoder(obj.read('vehicles.json'))

    for i in control.get_list_vehicle():
        print(i)

    main(control)
