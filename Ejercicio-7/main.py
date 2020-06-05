#   72 max spaces
#   Program Template
#   @author: Ezequiel

import keyboard #module extern: pip3 install keyboard
import os
import colorama
import time
from colorama import Fore, Back
import csv

from teacher import Teacher
from investigator import Investigator
from teacher_investigator import TeacherInvestigator
from support import Support
from control_personal import ControlPersonal

#Color Configuration
COLOR_OFF = Fore.GREEN
COLOR_ON = Fore.RED

def option1(control):
    print(control)

    input('\n\n<< press any key to continue >>')

def option2():

    input('\n\n<< press any key to continue >>')

def option3():

    input('\n\n<< press any key to continue >>')

#   Carga de un archivo CSV

def load_file_csv(control):
    file = open('personal.csv')
    reader = csv.reader(file, delimiter = ',')

    for row in reader:
        if len(row) == 7:
        	personal = Investigator(*row)

        elif len(row) == 6:
        	personal = Support(*row)

        elif len(row) == 12:
        	personal = TeacherInvestigator(*row)

        elif len(row) == 8:
        	personal = Teacher(*row)
    
        control.get_list_personal().add_end(personal)

    file.close()

select = {1: option1, 2: option2, 3: option3}

def menu(opc):
    input()
    func = select.get(opc, lambda: print(" * Opcion Incorrecta *"))
    func()

def set_color(opc_active, opc_select):
    color = '  ' + COLOR_OFF
    if opc_active == opc_select : color = '  ' + COLOR_ON + ' >'
    return color

def main():
	#Menu Configuration
    opc, max_opc = 1, 3
    flag = False

    while not flag:
        os.system('cls')
        print(COLOR_ON + '\n\tMenu Template\n')
        print(set_color(opc, 1) + '  option 1')
        print(set_color(opc, 2) + '  option 2')
        print(set_color(opc, 3) + '  option 3')
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
                menu(opc)
                
            else : flag = True
            time.sleep(0.1)

if __name__ == "__main__":
    colorama.init()
    colorama.init(autoreset=True)

    control = ControlPersonal()
    personal = TeacherInvestigator('25-44892692-3','James','DaVinci','34300','5','Geologia', 
        'Profesor Asociado','Analisis Matematico I','Medicina','Desarrollo de Vacuna COVID-19', 'Categoria 1', '2130')

    #load_file_csv(control)

    obj = ObjectEncoder()
    control = obj.Decoder(obj.read('personal.json'))

    for i in control.get_list_personal():
        print(i)

    #main()
