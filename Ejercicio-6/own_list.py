#	Lista implementada

from interface import IElement
import zope


class Node:
	__element = None
	__next = None

	def __init__(self, element):
		self.__element = element
		self.__next = None

	def __str__(self):
		return '{}'.format(self.__element)

	def _get_element(self):
		return self.__element

	def _get_next(self):
		return self.__next

	def _set_next(self, next):
		self.__next = next

	def _set_element(self, element):
		self.__element = element

@zope.interface.implementer(IElement)
class OwnList(Node):
	__head = None
	__current = None
	__index = 0
	__top = 0

	def __init__(self):
		self.__head = None
		self.__current = None

	def __str__(self):
		str_q = '['

		for i in self:
			str_q = str_q + ',{}'.format(i)

		return str_q + ']'

	def __len__(self):
		return self.__top

	def __iter__(self):
		return self

	def __next__(self):
		if self.__index == self.__top:
			self.__current = self.__head
			self.__index = 0
			raise StopIteration
		
		else:
			self.__index += 1
			obj = self.__current._get_element()
			self.__current = self.__current._get_next()
			return obj

#	Instance methods

#	Agregar elemento al final
	def add_end(self, element):
		new_node = Node(element)
		aux = self.__head

		if self.__head is None:
			self.__head = new_node
			self.__current = new_node
			self.__top += 1

		else:
			self.__top += 1

			while aux != None:
				before_node = aux
				aux = aux._get_next()

			before_node._set_next(new_node)

#	Agregar elemento al principio
	def add_beg(self, element):
		new_node = Node(element)
		new_node._set_next(self.__head)
		self.__head = new_node
		self.__current = new_node
		self.__top += 1

#	Agregar elemento en cualquier posicion dada
	def insert(self, index, element):
		if index > 0 and index < self.__top:
			new_node = Node(element)
			aux = self.__head
			i = 0

			while i < index and aux != None:
				before_node = aux
				aux = aux._get_next()
				i += 1

			aux_before = before_node._get_next()
			before_node._set_next(new_node) 
			new_node._set_next(aux_before)
			self.__top += 1

		elif index == 0:
			self.add_beg(element)

		elif index == self.__top:
			self.add_end(element)


#	Obtener elemento de una posicion
	def get(self, index):
		i = 0
		aux = self.__head

		while i != self.__top and index != i:
			aux = aux._get_next()
			i += 1

		if i != self.__top:
			return aux._get_element()
		else: print('index out of range')
