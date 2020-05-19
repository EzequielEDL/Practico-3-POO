#Ejercicio 1

from ManejaLibros import ManejaLibros
import keyboard #module extern: pip3 install keyboard
import os
import colorama
import time
from colorama import Fore, Back

#Color Configuration
COLOR_OFF = Fore.GREEN
COLOR_ON = Fore.RED

def option1(manejador):
    id = int(input(' Ingresar identificador de Libro: \n'))
    id = id - 10001
    manejador.showLibro(id)

    input('\n\n<< press any key to continue >>')

def option2(manejador):
    word = input(' Ingresar una palabra: \n')
    manejador.showAutor(word)
    
    input('\n\n<< press any key to continue >>')

select = {1: option1, 2: option2}

def menu(opc, manejador):
    input()
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func(manejador)

def setColor(opcActive, opcSelect):
    color = COLOR_OFF
    if opcActive == opcSelect : color = COLOR_ON
    return color

if __name__ == "__main__":
    colorama.init()
    colorama.init(autoreset=True)

    #Menu Configuration
    opc, MAX = 1, 3
    flag = False

    manejador = ManejaLibros('libros.csv')

    while not flag:
        os.system('cls')

        print(COLOR_ON + '\n\tMenu de Opciones\n')
        print(setColor(opc, 1) + '  - Mostrar un libro -')
        print(setColor(opc, 2) + '  - Mostrar autor/es -')
        print(setColor(opc, 3) + '  - Salir -')

        key = keyboard.read_key()
        print('\n  ' + key)
        if key == 'flecha abajo' and opc < MAX:            
            opc = opc + 1
            time.sleep(0.3)

        if key == 'flecha arriba' and opc > 1:
            opc = opc - 1
            time.sleep(0.3)

        if key == 'enter':
            if opc != 3 :
                menu(opc, manejador)
            else : flag = True
            time.sleep(0.3)
