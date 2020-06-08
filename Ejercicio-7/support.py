#	Clase de personal de apoyo

from personal import Personal


class Support(Personal):
	__category = ''

	def __init__(self, cuil, lastname, name, salary_basic, antiquity,
			category):
		self.__category = int(category)
		super().__init__(cuil, lastname, name, salary_basic, antiquity)
		
	def __str__(self):
		return super().__str__() + ' ■ {:<30} ■'.format(self.__category)

#	Convert to JSON
	def toJSON(self):
		d = dict(
			__class__ = self.__class__.__name__,
			__attributes__ = dict(
							category = self.__category
							)
						)
		d.get('__attributes__').update(super().toJSON().get('__attributes__'))
		return d

#	Instance methods

	def get_category(self):
		return self.__category

	def set_category(self, category):
		self.__category = category

	def get_salary(self):
		salary = self.get_salary_basic()
		
		if self.__category <= 10:
			salary *= 0.1

		elif self.__category <= 20:
			salary *= 0.2

		else:
			salary *= 0.3

		salary += self.get_salary_basic() * (self.get_antiquity() * 0.1)
		return salary