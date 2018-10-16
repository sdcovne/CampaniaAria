import csv
import geocoder

def geolocate(city):

    g = geocoder.google(city)

    return g.latlng

comuni = csv.reader(open("comuni.csv", 'r'))

comuni_lst = [ c[0] for c in comuni]

comuni_coords = []


for comune in comuni_lst:

    comune_coord = []
    comune_coord.append(comune)
    coord = geolocate(comune)
    if coord != None:
        for i in [0,1]:
            comune_coord.append(coord[i])
    else:
        comune_coord.append(coord)
    comuni_coords.append(comune_coord)


with open("comuni_coordinate.csv", 'w') as f:
    writer = csv.writer(f)
    for el in comuni_coords:
        writer.writerow(el)
