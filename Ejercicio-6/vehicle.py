#	Clase vehiculos nuevos
#	__model, __doors, __color, __price_base, brand, __version

import abc


class Vehicle:
	__model = ''
	__doors = ''
	__color = ''
	__price_base = 0.0

	def __init__(self, model, doors, color, price_base):
		self.__model = model
		self.__doors = doors
		self.__color = color
		self.__price_base = float(price_base)

	def __str__(self):
		return ' ■ {:<8} ■ {} ■ {:<8} ■ {:<9} ■ {:<9} '.format(
			self.__model, self.__doors, self.__color, self.__price_base, 
			self.get_price())

#	Instance methods
	
	def get_price(self):
		percentage = self.__price_base * self._get_percentage()
		return self.__price_base - percentage

	def get_model(self):
		return self.__model

	def get_doors(self):
		return self.__doors

	def get_color(self):
		return self.__color

	def get_price_base(self):
		return self.__price_base

	def set_model(self, model):
		self.__model = model

	def set_doors(self, doors):
		self.__doors = doors

	def set_color(self, color):
		self.__color = color

	def set_price_base(self, price_base):
		self.__price_base = price_base

#	Abstract methods
	@abc.abstractmethod	
	def _get_percentage(self):
		pass