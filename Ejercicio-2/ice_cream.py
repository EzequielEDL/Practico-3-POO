#	Clase de Helado

class IceCream:
	__grams = 0.0
	__flavors = None

	def __init__(self, grams, flavors):
		self.__grams = int(grams)
		self.__flavors = flavors

	def __str__(self):
		return '{}'.format(self.__grams)

#	Instance mehotds

	def get_flavors(self):
		return self.__flavors

	def get_grams(self):
		return self.__grams

	def set_grams(self, grams):
		self.__grams = grams
