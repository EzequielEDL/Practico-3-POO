#	SubClase Vehiculos viejos/usados
#	__patent, __year, __kilomoters

from vehicle import Vehicle
from datetime import datetime


class VehicleOld(Vehicle):
	__brand = ''
	__patent = ''
	__year = None
	__kilomoters = 0

	def __init__(self, model, doors, color, price_base, brand, patent,
			year, kilomoters):
		super().__init__(model, doors, color, price_base)
		self.__brand = brand
		self.__patent = patent
		self.__year = datetime(int(year), 1, 1)
		self.__kilomoters = int(kilomoters)

	def __str__(self):
		return super().__str__() + '■ {:<10} ■ {:<7} ■ {:<5} ■ {:<7} '.format(
			self.__brand, self.__patent, self.__year.year,
			self.__kilomoters)

#	Convert to JSON
	def toJSON(self):
		return dict(
			__class__ = self.__class__.__name__,
			__attributes__ = dict(
							model = self.get_model(),
							doors = self.get_doors(),
							color = self.get_color(),
							price_base = self.get_price_base(),
							brand = self.__brand,
							patent = self.__patent,
							year =  self.__year.year,
							kilomoters = self.__kilomoters
							)
						)

#	Instance methods

	def _get_percentage(self):
		percentage = 0.01 * (datetime.now().year - self.__year.year)
		
		if self.__kilomoters > 100000:
			percentage = percentage + 0.02

		return percentage

	def get_patent(self):
		return self.__patent

	def get_year(self):
		return self.__year

	def get_kilomoters(self):
		return self.__kilomoters

	def get_brand(self):
		return self.__brand

	def set_patent(self, patent):
		self.__patent = patent

	def set_year(self, year):
		self.__year = year

	def set_kilomoters(self, kilomoters):
		self.__kilomoters = kilomoters

	def set_brand(self, brand):
		self.__brand = brand
