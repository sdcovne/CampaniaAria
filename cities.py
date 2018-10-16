import csv

class City:
    def __init__(self, name, coordinates):
        self.name = name
        self.lat = coordinates[0]
        self.long = coordinates[1]


data_file = csv.reader(open("csv/coordinates.csv", 'r'))

loc_list = []

for data in data_file:
    city_name = data[0]
    city_lat = float(data[2])
    city_long = float(data[3])
    city_coordinates = [x for x in [city_lat, city_long]]
    city = City(city_name, city_coordinates)
    loc_list.append(city)
