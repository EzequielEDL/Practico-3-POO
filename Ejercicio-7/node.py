#	Clase Nodo

class Node:
	__element = None
	__next = None

	def __init__(self, element):
		self.__element = element
		self.__next = None

	def __str__(self):
		return '{}'.format(self.__element)

	def get_element(self):
		return self.__element

	def get_next(self):
		return self.__next

	def set_next(self, next):
		self.__next = next

	def set_element(self, element):
		self.__element = element
