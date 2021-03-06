import json
from control_vehicle import ControlVehicle
from vehicle_new import VehicleNew
from vehicle_old import VehicleOld

class ObjectEncoder(object):
	def save(self, dictionary, file):
		with open(file, 'w', encoding = 'UTF-8') as rute:
			json.dump(dictionary, rute, indent = 4)
			rute.close()

	def read(self, file):
		with open(file, encoding = 'UTF-8') as origin:
			dictionary = json.load(origin)
			origin.close()
			return dictionary

	def Decoder(self, d):
		if '__class__' not in d:
			return d
		else :
			class_name = d['__class__']
			class_ = eval(class_name)

			if class_name == 'ControlVehicle':
				elements = d['data']
				list_file = class_()

				for i in range(len(elements)):
					d_element = elements[i]
					class_name = d_element.pop('__class__')
					class_ = eval(class_name)
					attributes = d_element['__attributes__']
					a_vehicle = class_(**attributes)
					list_file.get_list_vehicle().add_end(a_vehicle)

				return list_file
