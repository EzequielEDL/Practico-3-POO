#	Clase de investigador

from personal import Personal


class Investigator(Personal):
	__area_inv = ''
	__type_inv = ''

	def __init__(self, **kw_args):
		self.__area_inv = str(kw_args.pop('area_inv'))
		self.__type_inv = str(kw_args.pop('type_inv'))
		super().__init__(**kw_args)
		
	def __str__(self):
		return super().__str__() + ' ■ {:<10} ■ {:<17} ■'.format(self.__area_inv,
			self.__type_inv)

#	Convert to JSON
	def toJSON(self):
		d = dict(
			__class__ = self.__class__.__name__,
			__attributes__ = dict(
							area_inv = self.__area_inv,
							type_inv = self.__type_inv
							)
						)
		d.get('__attributes__').update(super().toJSON().get('__attributes__'))
		return d

#	Instance methods

	def get_area_inv(self):
		return self.__area_inv

	def get_type_inv(self):
		return self.__type_inv

	def set_area_inv(self, area_inv):
		self.__area_inv = area_inv

	def set_type_inv(self, type_inv):
		self.__type_inv = type_inv

	def get_salary(self):
		return self.get_salary_basic() * (0.1 * self.get_antiquity())