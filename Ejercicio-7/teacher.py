#	Clase de Docente

from personal import Personal


class Teacher(Personal):
	__career = ''
	__position = ''
	__professorship = ''

	def __init__(self, cuil, lastname, name, salary_basic, antiquity,
			career, position, professorship):
		super().__init__(cuil, lastname, name, salary_basic, antiquity)
		self.__career = str(career)
		self.__position = str(position)
		self.__professorship = str(professorship)

	def __str__(self):
		return super().__str__() + ' ■ {} ■ {} ■ {}'.format(
			self.__career, self.__position, self.__professorship)

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
							career = self.__career,
							position = self.__position,
							professorship = self.__professorship
							)
						)

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
