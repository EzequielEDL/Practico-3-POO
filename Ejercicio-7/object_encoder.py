import json
from teacher_investigator import TeacherInvestigator
from control_personal import ControlPersonal
from investigator import Investigator
from teacher import Teacher
from support import Support


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

	def decoder(self, d):
		if '__class__' not in d:
			return d
		else :
			class_name = d['__class__']
			class_ = eval(class_name)

			if class_name == 'ControlPersonal':
				elements = d['data']
				list_file = class_()

				for i in range(len(elements)):
					d_element = elements[i]
					class_name = d_element.pop('__class__')
					class_ = eval(class_name)
					attributes = d_element['__attributes__']
					a_personal = class_(**attributes)
					list_file.get_list_personal().add_end(a_personal)

				return list_file
