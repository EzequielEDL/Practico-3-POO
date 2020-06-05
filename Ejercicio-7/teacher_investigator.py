#	Clase de docente investigador

from teacher import Teacher
from investigator import Investigator


class TeacherInvestigator(Teacher, Investigator):
	__category_inv = ''
	__salary_extra = 0.0

	def __init__(self, cuil, lastname, name, salary_basic, antiquity,
			career, position, professorship, area_inv, type_inv,
			category_inv, salary_extra):
		super().__init__(cuil, lastname, name, salary_basic, antiquity, career, position, professorship, area_inv, type_inv)
		self.__category_inv = str(category_inv)
		self.__salary_extra = float(salary_extra)

	def __str__(self):
		return super().__str__() + ' ■ {} ■ {}'.format(
			self.__category_inv, self.__salary_extra)

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
							career = self.get_career(),
							position = self.get_position(),
							professorship = self.get_professorship(),
							area = self.get_area(),
							type_inv = self.get_type_inv(),
							category_inv = self.__category_inv,
							salary_extra = self.__salary_extra
							)
						)

#	Instance methods

	def get_category_inv(self):
		return self.__category_inv

	def get_salary_extra(self):
		return self.__salary_extra

	def set_category_inv(self, category_inv):
		self.__category_inv = category_inv

	def set_salary_extra(self, salary_extra):
		self.__salary_extra = salary_extra
