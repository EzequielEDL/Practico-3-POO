#	SubClase Vehiculos viejos/usados
#	__patent, __year, __kilomoters

from vehicle import Vehicle


class VehicleOld(Vehicle):
	__patent = ''
	__year = ''
	__kilomoters = 0

	def __init__(self, model, doors, color, price_base, brand, patent,
			year, kilomoters):
		super().__init__(model, doors, color, price_base, brand)
		self.__patent = patent
		self.__year = year
		self.__kilomoters = kilomoters

	def __str__(self):
		return super().__str__() + '{:<7}║{:<5}║{:<7}║'.format(self.__patent, 
			self.__year, self.__kilomoters)

	def get_patent(self):
		return self.__patent

	def get_year(self):
		return self.__year

	def get_kilomoters(self):
		return self.__kilomoters

	def set_patent(self, patent):
		self.__patent = patent

	def set_year(self, year):
		self.__year = year

	def set_kilomoters(self, kilomoters):
		self.__kilomoters = kilomoters
