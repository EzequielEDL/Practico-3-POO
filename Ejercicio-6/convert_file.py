import csv
from vehicle import Vehicle
from vehicle_new import VehicleNew
from vehicle_old import VehicleOld


def load_file():
	list_r = []
	file = open('vehicles.csv')
	reader = csv.reader(file, delimiter = ',')
	for row in reader:
		if len(row) <= 6:
			vehicle = VehicleNew(row[0], row[1], row[2], float(row[3]),
				row[4], row[5])
		else:
			vehicle = VehicleOld(row[0], row[1], row[2], float(row[3]),
				row[4], row[5], row[6], int(row[7]))

		list_r.append(vehicle)

	file.close()
	return list_r

def show_list(list_r):
	for i in list_r:
		print(i)

def gen_jsonfile(list_r):

def main():
	vehicle_list = load_file()
	show_list(vehicle_list)


if __name__ == '__main__':
	main()