#	Clase de Personal
import abc


class Personal(abc.ABC):
	__cuil = ''
	__lastname = ''
	__name = ''
	__salary_basic = 0.0
	__antiquity = 0

	def __init__(self, cuil, lastname, name, salary_basic, antiquity):
		self.__cuil =  str(cuil)
		self.__lastname = str(lastname)
		self.__name = str(name)
		self.__salary_basic = float(salary_basic)
		self.__antiquity = int(antiquity)

	def __str__(self):
		return ' ■ {:<13} ■ {:<10} ■ {:<9} ■ {} ■ {:<2}'.format(
			self.__cuil, self.__lastname, self.__name,
			self.__salary_basic, self.__antiquity)

#	Instance methods

	def get_cuil(self):
		return self.__cuil

	def get_lastname(self):
		return self.__lastname

	def get_name(self):
		return self.__name

	def get_salary_basic(self):
		return self.__salary_basic

	def get_antiquity(self):
		return self.__antiquity

	def set_cuil(self, cuil):
		self.__cuil = cuil

	def set_lastname(self, lastname):
		self.__lastname = lastname

	def set_name(self, name):
		self.__name = name

	def set_salary_basic(self, salary_basic):
		self.__salary_basic = salary_basic

	def set_antiquity(self, antiquity):
		self.__antiquity = antiquity

	def toJSON(self):
		return dict(
			__attributes__ = dict(
							cuil = self.__cuil,
							lastname = self.__lastname,
							name = self.__name,
							salary_basic = self.__salary_basic,
							antiquity = self.__antiquity,
							)
						)

#	Abstract methods

	@abc.abstractmethod	
	def get_salary(self):
		pass