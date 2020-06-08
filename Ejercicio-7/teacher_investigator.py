#	Clase de docente investigador

from teacher import Teacher
from investigator import Investigator


class TeacherInvestigator(Teacher, Investigator):
	__category_inv = ''
	__salary_extra = 0.0

	def __init__(self, **kw_args):
		self.__category_inv = str(kw_args.pop('category_inv').upper())
		self.__salary_extra = float(kw_args.pop('salary_extra'))
		super().__init__(**kw_args)

	def __str__(self):
		str_q = ' ■ {:<11} ■ {:<10} ■ {:<9} ■ {} ■ {:<2}'.format(
			super().get_cuil(), super().get_lastname(),
			super().get_name(), super().get_salary_basic(),
			super().get_antiquity())
		str_q += ' ■ {:<10} ■ {:<17} ■ {:<23}'.format(
			super().get_career(), super().get_position(),
			super().get_professorship())
		str_q += ' ■ {:<10} ■ {:<20}'.format(
			super().get_area_inv(), super().get_type_inv())
		str_q += ' ■ {} ■ {}'.format(
			self.__category_inv, self.__salary_extra)
		
		return str_q

	def show(self):
		return super().__str__() + ' ■ {} ■ {}'.format(
			self.__category_inv, self.__salary_extra)

#	Convert to JSON
	def toJSON(self):
		d = dict(
			__class__ = self.__class__.__name__,
			__attributes__ = dict(
							category_inv = self.__category_inv,
							salary_extra = self.__salary_extra
							)
						)
		d.get('__attributes__').update(super().toJSON().get('__attributes__'))
		return d

#	Instance methods

	def get_category_inv(self):
		return self.__category_inv

	def get_salary_extra(self):
		return self.__salary_extra

	def set_category_inv(self, category_inv):
		self.__category_inv = category_inv

	def set_salary_extra(self, salary_extra):
		self.__salary_extra = salary_extra

	def get_salary_basic(self):
		return super().get_salary_basic() + self.__salary_extra

	def get_salary(self):
		return Teacher.get_salary(self) + self.__salary_extra
