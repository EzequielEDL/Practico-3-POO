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
