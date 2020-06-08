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

	def __getitem__(self, xi):
		if xi >= 0 and xi < len(self.__list_personal):
			return self.__list_personal[xi]

	def __sort_list(self, list_element, t):
		for i in range(len(list_element)): #ordenar por mayor
			j = i + 1

			for j in range(len(list_element) - 1):
				method1 = {'name': list_element[i].get_name(),
					'lastname': list_element[i].get_lastname()}
				method2 = {'name': list_element[j].get_name(),
					'lastname': list_element[j].get_lastname()}

				if method1[t] < method2[t]:
					aux = list_element[i]
					list_element[i] = list_element[j]
					list_element[j] = aux

	def __new_personal(self):
		name = input(' \244 Nombre: ')
		lastname = input(' \244 Apellido: ')
		cuil = input(' \244 CUIL: ')
		salary_basic = input(' \244 Salario basico: ')
		antiquity = input(' \244 Antiguedad: ')
		type_personal = input(' \244 Tipo de agente (Docente, Investigator, Apoyo, Docente investigador): ')

		d = {'cuil': cuil, 'lastname': lastname, 'name': name,
			'salary_basic': salary_basic, 'antiquity': antiquity}

		if type_personal.lower() == 'docente':
			career = input(' \244 Carrera: ')
			position = input(' \244 Cargo: ')
			professorship = input(' \244 Catedra: ')
			d.update({'career': career, 'position': position,
				'professorship': professorship})
			personal = Teacher(**d)

		elif type_personal.lower() == 'investigador':
			area_inv = input(' \244 Area de investigacion: ')
			type_inv = input(' \244 Tipo de investigacion: ')
			d.update({'area_inv': area_inv, 'type_inv': type_inv})
			personal = Investigator(**d)

		elif type_personal.lower() == 'apoyo':
			category = input(' \244 Categoria: ')
			d.update({'category': category})
			personal = Support(**d)

		elif type_personal.lower() == 'docente investigador':
			career = input(' \244 Carrera: ')
			position = input(' \244 Cargo: ')
			professorship = input(' \244 Catedra: ')
			area_inv = input(' \244 Area de investigacion: ')
			type_inv = input(' \244 Tipo de investigacion: ')
			category_inv = input(' \244 Categoria de investigacion: ')
			salary_extra = input(' \244 Importe extra: ')
			d.update({'career': career, 'position': position,
				'professorship': professorship,'area_inv': area_inv,
				'type_inv': type_inv, 'category_inv': category_inv,
				'salary_extra': salary_extra})
			personal = TeacherInvestigator(**d)

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

	def get_list_tchinv(self, career):
		list_tchinv = OwnList()

		for i in self.__list_personal:
			if isinstance(i, TeacherInvestigator):
				if i.get_career().lower() == career:
					list_tchinv.add_end(i)

		self.__sort_list(list_tchinv, 'name')
		return list_tchinv

	def list_area_inv(self, area_inv):
		cout_i = 0
		cout_ti = 0

		for i in self.__list_personal:
			if isinstance(i, Investigator):
				if not isinstance(i, TeacherInvestigator) and i.get_area_inv() == area_inv:
					cout_i += 1
				
				elif isinstance(i, TeacherInvestigator) and i.get_area_inv() == area_inv:
					cout_ti += 1

		print('\n * Investigadores: {}\n * Docentes Investigadores: {}'.format(
			cout_i, cout_ti))

	def list_type_personal(self):
		self.__sort_list(self.__list_personal, 'lastname')
		t = ''
		
		for i in self.__list_personal:
			if isinstance(i, Teacher) and not isinstance(t, TeacherInvestigator):
				t = 'Docente'

			elif isinstance(i, Investigator) and not isinstance(t, TeacherInvestigator):
				t = 'Investigador'

			elif isinstance(i, Support): t = 'Personal de apoyo'

			elif isinstance(i, TeacherInvestigator): t = 'Docente investigador'

			print(' ■ {:<13} ■ {:<10} ■ {:<20} ■ {} ■'.format(i.get_name(),
				i.get_lastname(), t, i.get_salary()))

	def list_cat_inv(self, category):
		acum = 0.0

		for i in self.__list_personal:
			if isinstance(i, TeacherInvestigator):
				if i.get_category_inv().lower() == category:
					print(' ■ {:<10} ■ {:<13} ■ {} ■'.format(i.get_name(),
					i.get_lastname(), i.get_salary_extra()))
					acum += i.get_salary_extra()

		print('\n * Importe extra total a pagar: {}'.format(acum))
