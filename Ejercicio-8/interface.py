#   72 max spaces
#   Ejercicio 5
#   @author: Ezequiel

from zope.interface import Interface


class ITreasurer(Interface):
#	Gastos de sueldo por empleado
	def show_salary(dni):
		pass

class IManager(Interface):
#	Modificar sueldo basico
	def mod_salary_basic(dni, salary_basic):
		pass

#	Modificar monto viatico
	def mod_amount_viatic(dni, amount_viatic):
		pass

#	Modificar valor por hora
	def mod_hour_price(hour_price):
		pass
