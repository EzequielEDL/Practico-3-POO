#	Clase manejador de helados

from control_flavor import ControlFlavor
from ice_cream import IceCream


class ControlIceCream:
	__list_ice_cream = None
	__control_flavor = None

	def __init__(self):
		self.__list_ice_cream = []
		self.__control_flavor = ControlFlavor()

#	Instance methods
	
	def add_list_ice_cream(self, grams, flavors):
		list_flavor = []

		for i in flavors:
			flavor = self.__control_flavor.get_list_flavor()[i - 1]
			list_flavor.append(flavor)

		ice_cream = IceCream(grams, list_flavor)
		self.__list_ice_cream.append(ice_cream)

	def get_control_favor(self):
		return self.__control_flavor

	def get_list_ice_cream(self):
		return self.__list_ice_cream

	def get_control_flavor(self):
		return self.__control_flavor

	def add_ice_cream(self):
		grams = int(input(' Tipo de Helado (100gr, 150gr, 250gr, 500gr y 1000gr): '))
		list_flavor = []

		if grams == 100 or  grams == 150 or  grams == 500 or  grams == 1000 :
			print(' flavors (MAX 4) - Finalizar con 0\n')
			number = int(input(' Sabor: '))

			while len(list_flavor) < 4 and number != 0:
				flavor = self.__control_flavor.get_list_flavor()[number - 1]
				list_flavor.append(flavor)

				if len(list_flavor) < 4 : number = int(input(' Sabor: '))

			print('\n - Venta Realizada -')
			ice_cream = IceCream(grams, list_flavor)
			self.__list_ice_cream.append(ice_cream)

		else:
			print('\nERROR - Tipo de Helado Incorrecto')

	def show_flavors_request(self, max):
		request = [[i, 0] for i in range(len(self.__control_flavor))]

		print(request)

		for i in self.__list_ice_cream:
			for j in i.get_flavors():
				request[j.get_number() - 1][1] += 1

		for i in range(len(request)): #ordenar por mayor
			j = i + 1
			for j in range(len(request)):
				if request[i][1] > request[j][1]:
					aux = request[i]
					request[i] = request[j]
					request[j] = aux

		for i in range(0, max):
			print('Pedidos: {:<2} - Sabor: {}'.format(request[i][1],
				self.__control_flavor.get_list_flavor()[request[i][0]]))

	def get_grams_flavor(self, number):
		acum_gram = 0

		for i in self.__list_ice_cream:
			for j in i.get_flavors():
				if number == j.get_number():
					acum_gram += i.get_grams() // len(i.get_flavors())

		return acum_gram

	def get_grams_ice(self, grams):
		number_flavor = []

		for i in self.__list_ice_cream:
			if i.get_grams() == grams:
				for j in i.get_flavors():
					if not j.get_number() in number_flavor:
						number_flavor.append(j.get_number())

		for i in range(len(number_flavor)):
			print(' {}'.format(self.__control_flavor.get_list_flavor()[i]))
