#Ejercico 2

import keyboard #module extern: pip3 install keyboard
import os
import colorama
import time
from colorama import Fore, Back

from ManejaHelados import ManejaHelados
from ManejaSabores import ManejaSabores
from Helado import Helado

#Color Configuration
COLOR_OFF = Fore.GREEN
COLOR_ON = Fore.RED

def option1(manejaHelados, manejaSabores):
    print(manejaSabores)
    manejaHelados.regVenta()

    input('\n\n<< press any key to continue >>')

def option2(manejaHelados, manejaSabores):
    print('\n Lista de los 5 Sabores mas pedidos: \n')
    manejaHelados.showSaboresPedidos(5)

    input('\n\n<< press any key to continue >>')

def option3(manejaHelados, manejaSabores):
    numSabor = int(input('\n Ingresar numero de sabor: '))
    print('\n Total de gramos vendidos: {}.gr'.format(manejaHelados.getSaboresGramos(numSabor)))

    input('\n\n<< press any key to continue >>')

def option4(manejaHelados, manejaSabores):
    tipoHelado = int(input('\n Ingresar tipo de helado (100gr, 150gr, 250gr, 500gr y 1000gr): '))
    manejaHelados.showHeladosTipos(tipoHelado)

    input('\n\n<< press any key to continue >>')

select = {1: option1, 2: option2, 3: option3, 4: option4}

def menu(opc, manejaHelados, manejaSabores):
    input()
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func(manejaHelados, manejaSabores)

def setColor(opcActive, opcSelect):
    color = COLOR_OFF
    if opcActive == opcSelect : color = COLOR_ON
    return color

def test(manejaHelados):
    
    #manejaSabores = ManejaSabores()
    os.system('cls')
    helado1 = Helado(100, [2,4,2,10])
    helado2 = Helado(100, [2,10,11,10])
    helado3 = Helado(100, [2,3,4,13])
    helado4 = Helado(100, [2,6,4,12])
    helado5 = Helado(100, [2,1,5,9])
    helado6 = Helado(100, [2,3,2,8])

    manejaHelados.addListVentas(helado1)
    manejaHelados.addListVentas(helado2)
    manejaHelados.addListVentas(helado3)
    manejaHelados.addListVentas(helado4)
    manejaHelados.addListVentas(helado5)
    manejaHelados.addListVentas(helado6)

    
    print('\n Total de gramos vendidos: {}.gr'.format(manejaHelados.getSaboresGramos(2)))
    #manejaHelados.showCountSabores(5)

    #input()


if __name__ == "__main__":
    colorama.init()
    colorama.init(autoreset=True)
    manejaHelados = ManejaHelados()
    manejaSabores = ManejaSabores()

    test(manejaHelados)


    #Menu Configuration
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
            time.sleep(0.3)

        if key == 'flecha arriba' and opc > 1:
            opc = opc - 1
            time.sleep(0.3)

        if key == 'enter':            
            if opc != 5 :
                key = 'a'
                menu(opc, manejaHelados, manejaSabores)
            else : flag = True
            time.sleep(0.3)
