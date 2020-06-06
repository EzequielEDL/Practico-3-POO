#	Clase de investigador

from personal import Personal


class Investigator(Personal):
	__area_inv = ''
	__type_inv = ''

	def __init__(self, cuil, lastname, name, salary_basic, antiquity,
			career, position, professorship, area_inv, type_inv):
		super().__init__(cuil, lastname, name, salary_basic, antiquity,
			career, position, professorship, area_inv, type_inv)
		self.__area_inv = str(area_inv)
		self.__type_inv = str(type_inv)
		
	def __str__(self):
		return super().__str__() + ' ■ {:<10} ■ {:<17} ■'.format(self.__area_inv,
			self.__type_inv)

#	Convert to JSON
	def toJSON(self):
		return dict(
			__class__ = self.__class__.__name__,
			__attributes__ = dict(
							cuil = self.get_cuil(),
							lastname = self.get_lastname(),
							name = self.get_name(),
							salary_basic = self.get_salary_basic(),
							antiquity = self.get_antiquity(),
							career = '',
							position = '',
							professorship = '',
							area_inv = self.__area_inv,
							type_inv = self.__type_inv
							)
						)

#	Instance methods

	def get_area_inv(self):
		return self.__area_inv

	def get_type_inv(self):
		return self.__type_inv

	def set_area_inv(self, area_inv):
		self.__area_inv = area_inv

	def set_type_inv(self, type_inv):
		self.__type_inv = type_inv
