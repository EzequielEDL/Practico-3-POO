#Ejercico 3

import keyboard #module extern: pip3 install keyboard
import os
import colorama
import time
from colorama import Fore, Back

from ManejaTaller import ManejaTaller
from ManejaPersona import ManejaPersona
from ManejaInscripcion import ManejaInscripcion

from TallerCapacitacion import TallerCapacitacion
from Persona import Persona
from Inscripcion import Inscripcion

#Color Configuration
COLOR_OFF = Fore.GREEN
COLOR_ON = Fore.RED

def option1(manejaTaller, manejaPersona, manejaInscripcion):
    print(manejaTaller)
    nombre = input(' \244 Ingresar nombre: ')
    direccion = input(' \244 Ingresar direccion: ')
    dni = input(' \244 Ingresar DNI: ')
    idTaller = int(input(' \244 Ingresar el ID del Taller: '))
    persona = Persona(nombre, direccion, dni)

    inscripcion = manejaTaller.inscribirPersona(persona, idTaller)
    if inscripcion != None :
        manejaPersona.addListPersona(persona)
        manejaInscripcion.addArrayInscripcion(inscripcion)
        print(' * Inscripcion realizada !')
    else : print(' * No hay vacantes disponible')

    input('\n\n<< press any key to continue >>')

def option2(manejaTaller, manejaPersona, manejaInscripcion):
    dni = input(' \244 Ingresar DNI: ')
    manejaInscripcion.consultarInscripcion(dni)

    input('\n\n<< press any key to continue >>')

def option3(manejaTaller, manejaPersona, manejaInscripcion):
    idTaller = int(input(' \244 Ingresar ID del Taller: '))
    print('\n')
    manejaTaller.consultarInscripciones(idTaller)

    input('\n\n<< press any key to continue >>')

def option4(manejaTaller, manejaPersona, manejaInscripcion):
    dni = input(' \244 Ingresar DNI: ')
    manejaInscripcion.pagoInscripcion(dni)

    input('\n\n<< press any key to continue >>')

def option5(manejaTaller, manejaPersona, manejaInscripcion):
    manejaInscripcion.saveFile()

    input('\n\n<< press any key to continue >>')

select = {1: option1, 2: option2, 3: option3, 4:option4, 5:option5}

def menu(opc, manejaTaller, manejaPersona, manejaInscripcion):
    input()
    func = select.get(opc, lambda: print("Opcion Incorrecta"))
    func(manejaTaller, manejaPersona, manejaInscripcion)

def setColor(opcActive, opcSelect):
    color = '  ' + COLOR_OFF
    if opcActive == opcSelect : color = '  ' + COLOR_ON + ' >'
    return color

def test(manejaTaller, manejaPersona, manejaInscripcion):
    print(manejaTaller)

    persona1 = Persona('Jose', 'jose@gmail.com', '312837')
    persona2 = Persona('manuel', 'manu@gmail.com', '14938123')
    persona3 = Persona('ester', 'ester@hotmail.com', '123')
    
    inscripcion1 = manejaTaller.inscribirPersona(persona1, 2)
    inscripcion2 = manejaTaller.inscribirPersona(persona2, 3)
    inscripcion3 = manejaTaller.inscribirPersona(persona3, 4)

    manejaPersona.addListPersona(persona1)
    manejaPersona.addListPersona(persona2)
    manejaPersona.addListPersona(persona3)

    manejaInscripcion.addArrayInscripcion(inscripcion1)
    manejaInscripcion.addArrayInscripcion(inscripcion2)
    manejaInscripcion.addArrayInscripcion(inscripcion3)

    print(manejaPersona)

    print(' * Inscripcion realizada !')

    input()


if __name__ == "__main__":
    colorama.init()
    colorama.init(autoreset=True)

    manejaTaller = ManejaTaller()
    manejaPersona = ManejaPersona()
    manejaInscripcion = ManejaInscripcion()

    test(manejaTaller, manejaPersona, manejaInscripcion)

    #Menu Configuration
    opc, MAX = 1, 6
    flag = False

    while not flag:
        os.system('cls')

        print(COLOR_ON + '\n\tTalleres de Capacitacion\n')
        print(setColor(opc, 1) + ' Inscribir una persona en un taller')
        print(setColor(opc, 2) + ' Consultar inscripción')
        print(setColor(opc, 3) + ' Consultar inscriptos')
        print(setColor(opc, 4) + ' Registrar pago')
        print(setColor(opc, 5) + ' Guardar inscripciones')
        print(setColor(opc, 6) + ' Salir')

        key = keyboard.read_key()
        print('\n  ' + key)
        if key == 'flecha abajo' and opc < MAX:            
            opc = opc + 1
            time.sleep(0.1)

        if key == 'flecha arriba' and opc > 1:
            opc = opc - 1
            time.sleep(0.1)

        if key == 'enter':
            if opc != 6 :
                menu(opc, manejaTaller, manejaPersona, manejaInscripcion)
            else : flag = True
            time.sleep(0.1)