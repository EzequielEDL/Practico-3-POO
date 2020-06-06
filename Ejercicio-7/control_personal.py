#	Clase de manejador personal

from teacher import Teacher
from investigator import Investigator
from support import Support
from teacher_investigator import TeacherInvestigator
from own_list import OwnList


class ControlPersonal:
	__list_personal = None

	def __init__(self):
		self.__list_personal = OwnList()

	def __str__(self):
		str_q = ''
		for i in self.__list_personal:
			str_q = str_q + str(i) + '\n'

		return str_q

#	Conver to JSON
	def toJSON(self):
		personal = []

		for i in self.__list_personal:
			personal.append(i.toJSON())

		d = dict(
			__class__ = self.__class__.__name__,
			data = personal
			)

		return d

#	Instance methods

	def get_list_personal(self):
		return self.__list_personal

	def __sort_list(self, list_element, t):
		for i in range(len(list_element)): #ordenar por mayor
			j = i + 1

			for j in range(len(list_element)):
				method1 = {1: list_element[i].get_name(),
					2: list_element[i].get_lastname()}
				method2 = {1: list_element[j].get_name(),
					2: list_element[j].get_lastname()}

				if method1[t] < method2[t]:
					aux = list_element[i]
					list_element[i] = list_element[j]
					list_element[j] = aux

		return list_element

	def __new_personal(self):
		name = input(' \244 Nombre: ')
		lastname = input(' \244 Apellido: ')
		cuil = input(' \244 CUIL: ')
		salary_basic = input(' \244 Salario basico: ')
		antiquity = input(' \244 Antiguedad: ')
		type_personal = input(' \244 Tipo de agente (Docente, Investigator, Apoyo, Docente investigador): ')

		if type_personal.lower() == 'docente':
			career = input(' \244 Carrera: ')
			position = input(' \244 Cargo: ')
			professorship = input(' \244 Catedra: ')
			personal = Teacher(cuil, lastname, name, salary_basic,
				antiquity, career, position, professorship)

		elif type_personal.lower() == 'investigador':
			area_inv = input(' \244 Area de investigacion: ')
			type_inv = input(' \244 Tipo de investigacion: ')
			personal = Investigator(cuil, lastname, name, salary_basic,
				antiquity, '', '', '', area_inv, type_inv)

		elif type_personal.lower() == 'apoyo':
			category = input(' \244 Categoria: ')
			personal = Support(cuil, lastname, name, salary_basic,
				antiquity, category)

		elif type_personal.lower() == 'docente investigador':
			career = input(' \244 Carrera: ')
			position = input(' \244 Cargo: ')
			professorship = input(' \244 Catedra: ')
			area_inv = input(' \244 Area de investigacion: ')
			type_inv = input(' \244 Tipo de investigacion: ')
			category_inv = input(' \244 Categoria de investigacion: ')
			salary_extra = input(' \244 Importe extra: ')
			personal = TeacherInvestigator(cuil, lastname, name,
				salary_basic, antiquity,career, position, professorship,
				area_inv, type_inv, category_inv, salary_extra)

		else :
			print('\n * Error: tipo de agente inexistente')

		return personal

	def insert_personal(self, index):
	    if index > 0 and index < len(self.__list_personal):
	    	self.__list_personal.insert(index, self.__new_personal())
	    	print('\n * Agente agregado !')

	def add_personal(self, position):

		if position.lower() == 'final':
			self.__list_personal.add_end(self.__new_personal())
			print('\n * Agente agregado !')

		elif position.lower() == 'inicio':
			self.__list_personal.add_beg(self.__new_personal())
			print('\n * Agente agregado !')

		else :
			print('\n * Error: posicion invalida')

	def sort_list_last(self):

		for i in self.__list_personal:
			print(i)

		for i in self.__list_personal:
			for j in self.__list_personal:
				if i.get_lastname() < j.get_lastname():
					aux = i.get_lastname()
					i.set_lastname(j.get_lastname())
					j.set_lastname(aux)

		for i in self.__list_personal:
			print(i)




