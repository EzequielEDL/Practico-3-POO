#	SubClase Vehiculo nuevo
#	__version

from vehicle import Vehicle


class VehicleNew(Vehicle):
	brand = 'chevrolet'
	__version = ''

	def __init__(self, model, doors, color, price_base, version):
		super().__init__(model, doors, color, price_base)
		self.__version = version

	def __str__(self):
		return super().__str__() + '■ {:<10} ■ {:<7} '.format(self.brand,
			self.__version)

#	Convert to JSON
	def toJSON(self):
		return dict(
			__class__ = self.__class__.__name__,
			__attributes__ = dict(
							model = self.get_model(),
							doors = self.get_doors(),
							color = self.get_color(),
							price_base = self.get_price_base(),
							version = self.__version
							)
						)

#	Instance methods

	def _get_percentage(self):
		percentage = 0.1

		if self.__version == 'full':
			percentage = percentage + 0.02

		return percentage

	def get_version(self):
		return self.__version

	def get_brand(self):
		return self.brand

	def set_version(self, version):
		self.__version = version
