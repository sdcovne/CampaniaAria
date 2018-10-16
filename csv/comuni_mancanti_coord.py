import csv
import geocoder

def geolocate(city):

    g = geocoder.google(city)

    return g.latlng


comuni = csv.reader(open("comuni_mancanti_coord6.csv", "r"))

comuni_mancanti_lst = [comune[0] for comune in comuni if comune[1] == ""]


comuni_mancanti_coords = []

for comune_mancante in comuni_mancanti_lst:
    comune_mancante_coord = []
    coord = geolocate(comune_mancante)
    comune_mancante_coord.append(comune_mancante)
    if coord != None:
        comune_mancante_coord.append(coord[0])
        comune_mancante_coord.append(coord[1])
    else:
        comune_mancante_coord.append(coord)
    comuni_mancanti_coords.append(comune_mancante_coord)

with open("comuni_mancanti_coord7.csv", "w") as f:
    writer = csv.writer(f)
    for c in comuni_mancanti_coords:
        writer.writerow(c)