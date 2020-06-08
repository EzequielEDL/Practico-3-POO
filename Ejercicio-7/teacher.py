#	Clase de Docente

from personal import Personal


class Teacher(Personal):
	__career = ''
	__position = ''
	__professorship = ''

	def __init__(self, **kw_args):
		self.__career = str(kw_args.pop('career'))
		self.__position = str(kw_args.pop('position'))
		self.__professorship = str(kw_args.pop('professorship'))
		super().__init__(**kw_args)

	def __str__(self):
		return super().__str__() + ' ■ {:<10} ■ {:<17} ■ {}'.format(
			self.__career, self.__position, self.__professorship)

#	Convert to JSON
	def toJSON(self):
		d = dict(
			__class__ = self.__class__.__name__,
			__attributes__ = dict(
							career = self.__career,
							position = self.__position,
							professorship = self.__professorship
							)
						)
		d.get('__attributes__').update(super().toJSON().get('__attributes__'))
		return d

#	Instance methods

	def get_career(self):
		return self.__career

	def get_position(self):
		return self.__position

	def get_professorship(self):
		return self.__professorship

	def set_career(self, career):
		self.__career = career

	def set_position(self, position):
		self.__position = position

	def set_professorship(self, professorship):
		self.__professorship = professorship

	def get_salary(self):
		salary = self.get_salary_basic()

		if self.__position.lower() == 'simple': 
			salary += salary * 0.1

		elif self.__position.lower() == 'semiexclusivo':
			salary += salary * 0.2

		else:
			salary += salary * 0.5

		salary += self.get_salary_basic() * (0.1 * self.get_antiquity())
		return salary