#	SubClase Vehiculo nuevo
#	__version

from vehicle import Vehicle


class VehicleNew(Vehicle):
	brand = 'chevrolet'
	__version = ''

	def __init__(self, model, doors, color, price_base, brand, version):
		super().__init__(model, doors, color, price_base, brand)
		self.__version = version
		brand = brand

	def __str__(self):
		return super().__str__() + '{}║'.format(self.__version)

	def get_version(self):
		return self.__version

	def set_version(self, version):
		self.__version = version