#	Lista implementada

class Lista:
	__head = None

	def __init__(self):
		self.__head = None

	def __str__(self):
		aux = self.__head
		str_q = '['

		while aux != None:
			str_q = str_q + '{},'.format(aux)
			aux = aux.get_next_node()

		return str_q + ']'

	def add_end(self, object):
		new_node = Node(object)
		aux = self.__head

		if self.__head is None:
			self.__head = new_node

		else:
			while aux != None:
				before_node = aux
				aux = aux.get_next_node()

			before_node.set_next_node(new_node)


		def add_beg(self, object):
			new_node = Node(object)
			new_node.set_next_node(self.__head)
			self.__head = new_node

	#def del_index():
	#def index():





class Node:
	__object = None
	__next_node = None

	def __init__(self, object):
		self.__object = object
		self.__next_object = None

	def __str__(self):
		return '{}'.format(self.__object)

	def get_next_node(self):
		return self.__next_node

	def set_next_node(self, next_node):
		self.__next_node = next_node


