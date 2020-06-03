#	Clase Manejador de Vehiculo

from vehicle import Vehicle
from vehicle_new import VehicleNew
from vehicle_old import VehicleOld
from own_list import OwnList


class ControlVehicle:
	__list_vehicle = None

	def __init__(self):
		self.__list_vehicle = OwnList()

#	Conver to JSON
	def toJSON(self):
		vehicles = []

		for i in self.__list_vehicle:
			vehicles.append(i.toJSON())

		d = dict(
			__class__ = self.__class__.__name__,
			data = vehicles
			)

		return d

#	Instance methods

	def show_list(self):
		for i in self.__list_vehicle:
			print(i)

	def get_list_vehicle(self):
		return self.__list_vehicle

	def __new_vehicle(self):
		model = input(' \244 Modelo: ')
		doors = input(' \244 Cantidad de puertas: ')
		price_base = input(' \244 Precio base: ')
		color = input(' \244 Color: ')
		type_vehicle = input(' \244 Tipo de vehiculo (Nuevo/Usado): ')

		if type_vehicle.lower() == 'nuevo':
			version = input('\t \244 Version (full/base): ')
			vehicle = VehicleNew(model, doors, color, price_base, version)

		elif type_vehicle.lower() == 'usado':
			patent = input('\t \244 Patente: ')
			year = input('\t \244 Año: ')
			kilomoters = input('\t \244 Kilometraje: ')
			vehicle = VehicleOld(model, doors, color, price_base, patent, 
	            year, kilomoters, brand)

		return vehicle
		
	def insert_vehicle(self, index):
	    if index > 0 and index < len(self.__list_vehicle):
	    	self.__list_vehicle.insert(index, self.__new_vehicle())

	    print('\n * Vehiculo agregado !')

	def add_vehicle(self, position):

		if position.lower() == 'final':
			self.__list_vehicle.add_end(self.__new_vehicle())

		elif position.lower() == 'inicio':
			self.__list_vehicle.add_beg(self.__new_vehicle())

		print('\n * Vehiculo agregado !')

	def search_vehicle(self, patent):
		i, flag = 0, True

		while i < len(self.__list_vehicle) and flag:
			vehicle = self.__list_vehicle.get(i)

			if isinstance(vehicle, VehicleOld):
				if vehicle.get_patent() == patent:
					flag = False
					i -= 1

			i += 1

		if i <= len(self.__list_vehicle) - 1:
			return vehicle

	def list_cheap_vehicle(self):
		list_cheap = []
		minimum = 9999999999999

		for i in self.__list_vehicle:
			if i.get_price() < minimum:
				minimum = i.get_price()

		for i in self.__list_vehicle:
			if i.get_price() == minimum:
				list_cheap.append(i)

		return list_cheap



