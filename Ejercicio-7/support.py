#	Clase de personal de apoyo

from personal import Personal


class Support(Personal):
	__category = ''

	def __init__(self, cuil, lastname, name, salary_basic, antiquity,
			category):
		super().__init__(cuil, lastname, name, salary_basic, antiquity)
		self.__category = str(category)
		
	def __str__(self):
		return super().__str__() + ' ■ {:<30} ■'.format(self.__category)

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
							category = self.__category
							)
						)

#	Instance methods

	def get_category(self):
		return self.__category

	def set_category(self, category):
		self.__category = category
