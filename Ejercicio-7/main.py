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
from control_personal import ControlPersonal
from teacher import Teacher
from investigator import Investigator
from teacher_investigator import TeacherInvestigator
from support import Support

#Color Configuration
COLOR_OFF = Fore.GREEN
COLOR_ON = Fore.RED

def print_list(list_personal):
    j = 0
    print(' ┌{:─<92}┐'.format('─'))
    print(' │{:<2} ■ {:<13} ■ {:<10} ■ {:<9} ■ {:<7} ■ {:<36}│'.format(
        'i', 'CUIL', 'Nombre', 'Apellido', 'S. B.', 'A.'))

    for i in list_personal:
        st = str(i)
        print(' │{:<2}{:<92}'.format(j + 1, st))
        j += 1

    print(' └{:─<92}┘'.format('─'))
    print('\n * CANTIDAD DE AGENTES: {} \n'.format(
        len(list_personal)))

def option1(control):
    print_list(control.get_list_personal())
    index = int(input(' \244 Posicion: '))
    control.insert_personal(index - 1 )
    input('\n\n<< press any key to continue >>')

def option2(control):
    print_list(control.get_list_personal())
    position = input('\n \244 Al Final o Inicio: ')
    control.add_personal(position)
    input('\n\n<< press any key to continue >>')

def option3(control):
    print_list(control.get_list_personal())
    index = int(input(' \244 Posicion: '))
    t = control[index - 1]
    print('Tipo de agente: ', end = '')
    
    if isinstance(t, Teacher) and not isinstance(t, TeacherInvestigator):
        print('Docente')

    elif isinstance(t, Investigator) and not isinstance(t, TeacherInvestigator):
        print('Investigador')

    elif isinstance(t, Support): print('Personal de apoyo')

    elif isinstance(t, TeacherInvestigator): print('Docente investigador')

    input('\n\n<< press any key to continue >>')

def option4(control):
    career = input(' \244 Carrera: ')
    print_list(control.get_list_tchinv(career))
    input('\n\n<< press any key to continue >>')

def option5(control):
    area_inv = input(' \244 Area de investigacion: ')
    control.list_area_inv(area_inv)
    input('\n\n<< press any key to continue >>')

def option6(control):
    control.list_type_personal()
    input('\n\n<< press any key to continue >>')

def option7(control):
    category = input(' \244 Categoria de investigacion: ')
    control.list_cat_inv(category)
    input('\n\n<< press any key to continue >>')

def option8(control):
    obj.save(control.toJSON(), 'personal.json')
    print('\n * Datos almacenados !')

    input('\n\n<< press any key to continue >>')

#   Carga de un archivo CSV

def load_file_csv(control, obj):
    file = open('personal.csv')
    reader = csv.reader(file, delimiter = ',')

    for row in reader:
        d = {'cuil': row[0], 'lastname': row[1],
            'name': row[2], 'salary_basic': row[3],
            'antiquity': row[4]}

        if len(row) == 7:
            d.update({'area_inv': row[5], 'type_inv': row[6]})
            personal = Investigator(**d)

        elif len(row) == 6:
            d.update({'category': row[5]})
            personal = Support(**d)

        elif len(row) == 12:
            d.update({'career': row[5], 'position': row[6], 'professorship': row[7],
                'area_inv': row[8], 'type_inv': row[9], 'category_inv': row[10],
                'salary_extra': row[11]})
            personal = TeacherInvestigator(**d)

        elif len(row) == 8:
            d.update({'career': row[5], 'position': row[6], 'professorship': row[7]})
            personal = Teacher(**d)
    
        control.get_list_personal().add_end(personal)

    file.close()
    obj.save(control.toJSON(), 'personal.json')

select = {1: option1, 2: option2, 3: option3, 4: option4, 5: option5,
    6: option6, 7: option7, 8: option8}

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
    opc, max_opc = 1, 9
    flag = False

    while not flag:
        os.system('cls')
        print(COLOR_ON + '\n\tCentro de computos de la UNSJ\n')
        print(set_color(opc, 1) + '  1. Insertar a agente')
        print(set_color(opc, 2) + '  2. Agregar agente')
        print(set_color(opc, 3) + '  3. Mostrar agente')
        print(set_color(opc, 4) + '  4. Listado de doc.-inv.')
        print(set_color(opc, 5) + '  5. Area de investigacion')
        print(set_color(opc, 6) + '  6. Listado de agentes')
        print(set_color(opc, 7) + '  7. Categoria de investigacion')
        print(set_color(opc, 8) + '  8. Almacenar')
        print(set_color(opc, 9) + '  9. Salir')
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
    control = ControlPersonal()
    obj = ObjectEncoder()
    #load_file_csv(control, obj)
    control = obj.decoder(obj.read('personal.json'))
   


    for i in control.get_list_personal():
        print(i)

    main(control)
