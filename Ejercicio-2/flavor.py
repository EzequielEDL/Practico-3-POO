#	Clase de Sabor

class Flavor:
	__number = 0
	__name = ''
	__description = ''

	def __init__(self, number, name, description):
		self.__number = int(number)
		self.__name = str(name)
		self.__description = str(description)

	def __str__(self):
		return ' ■ {:<2} ■ {:<15} ■ {}'.format(self.__number, self.__name,
			self.__description)

#	Instance methods

	def get_number(self):
		return self.__number

	def get_name(self):
		return self.__name

	def get_description(self):
		return self.__description

	def set_number(self, number):
		self.__number = number

	def set_name(self, name):
		self.__name = name

	def set_description(self, description):
		self.__description = description