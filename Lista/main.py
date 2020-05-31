from lista import Lista

class num:
	__num = 0
	def __init__(self, num):
		self.__num = num

	def __str__(self):
		return '{}'.format(self.__num)

def main():
	lista = Lista()

	num1 = num(4)
	num2 = num(6)
	num3 = num(7)
	num4 = num(2)

	lista.add_end(num1)
	lista.add_end(num2)
	lista.add_end(num3)
	lista.add_end(num4)
	print(lista)

if __name__ == '__main__':
	main()