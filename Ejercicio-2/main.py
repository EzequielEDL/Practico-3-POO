#   72 max spaces
#   Program Template
#   @author: Ezequiel

import keyboard #module extern: pip3 install keyboard
import os
import colorama
import time
from colorama import Fore, Back

from control_ice_cream import ControlIceCream

#Color Configuration
COLOR_OFF = Fore.GREEN
COLOR_ON = Fore.RED

def option1(control):
    print(control.get_control_favor())
    control.add_ice_cream()

    input('\n\n<< press any key to continue >>')

def option2(control):
    print('\n Lista de los 5 Sabores mas pedidos: \n')
    control.show_flavors_request(5)

    input('\n\n<< press any key to continue >>')

def option3(control):
    number = int(input('\n Ingresar numero de sabor: '))
    print('\n Total de gramos vendidos: {}.gr'.format(control.get_grams_flavor(number)))

    input('\n\n<< press any key to continue >>')

def option4(control):
    grams = int(input('\n Ingresar tipo de helado (100gr, 150gr, 250gr, 500gr y 1000gr): '))
    control.get_grams_ice(grams)

    input('\n\n<< press any key to continue >>')

select = {1: option1, 2: option2, 3: option3, 4: option4}

def menu(opc, control):
    input()
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func(control)

def setColor(opcActive, opcSelect):
    color = COLOR_OFF
    if opcActive == opcSelect : color = COLOR_ON
    return color

def test(control):
    
    #manejaSabores = ManejaSabores()
    os.system('cls')
    control.add_list_ice_cream(100, [2,4,2,10])
    control.add_list_ice_cream(100, [2,4,2,10])
    control.add_list_ice_cream(100, [2,4,2,10])
    control.add_list_ice_cream(100, [1,10])
    control.add_list_ice_cream(100, [2,4,2])

    for i in control.get_list_ice_cream():
    	print('- Gramos: {}'.format(i))

    	for j in i.get_flavors():
    		print('\t{}'.format(j))


    #input()
def main():
#	Menu Configuration
    opc, MAX = 1, 5
    flag = False

    while not flag:
        os.system('cls')

        print(COLOR_ON + '\n\tHeladeria EL CONITO\n')
        print(setColor(opc, 1) + '  Registrar un helado vendido')
        print(setColor(opc, 2) + '  Mostrar el nombre de los 5 sabores de helado más pedidos')
        print(setColor(opc, 3) + '  Ingresar un número de sabor')
        print(setColor(opc, 4) + '  Ingresar tipo de helado')
        print(setColor(opc, 5) + '  Salir')

        key = keyboard.read_key()
        print('\n  ' + key)
        if key == 'flecha abajo' and opc < MAX:            
            opc = opc + 1
            time.sleep(0.1)

        if key == 'flecha arriba' and opc > 1:
            opc = opc - 1
            time.sleep(0.1)

        if key == 'enter':            
            if opc != 5 :
                key = 'a'
                menu(opc, control)
            else : flag = True
            time.sleep(0.1)

if __name__ == "__main__":
    colorama.init()
    colorama.init(autoreset=True)
    
    control = ControlIceCream()

    test(control)

    main()
