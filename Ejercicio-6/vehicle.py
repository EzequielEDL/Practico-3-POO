#	Clase vehiculos nuevos
#	__model, __doors, __color, __price_base, brand, __version

class Vehicle:
	__model = ''
	__doors = ''
	__color = ''
	__price_base = 0.0
	__brand = ''

	def __init__(self, model, doors, color, price_base, brand):
		self.__model = model
		self.__doors = doors
		self.__color = color
		self.__price_base = price_base
		self.__brand = brand

	def __str__(self):
		return '║{:<9}║{:<2}║{:<9}║{:<10}║{:<11}║'.format(self.__model, self.__doors,
			self.__color, self.__price_base, self.__brand)

#	Instance class

	def get_model(self):
		return self.__model

	def get_doors(self):
		return self.__doors

	def get_color(self):
		return self.__color

	def get_price_base(self):
		return self.__price_base

	def get_brand(self):
		return self.__brand

	def set_model(self, model):
		self.__model = model

	def set_doors(self, doors):
		self.__doors = doors

	def set_color(self, color):
		self.__color = color

	def set_price_base(self, price_base):
		self.__price_base = price_base

	def set_brand(self, brand):
		self.__brand = brand
