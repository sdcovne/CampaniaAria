import geocoder
import math
import requests
from bs4 import BeautifulSoup
import csv



def get_date():
    
    url = 'http://88.45.133.130/meteoambientecampania/php/pubblicazione_dati_centraline_valori_medi.php'

    data_page= requests.get(url)

    soup = BeautifulSoup(data_page.content, "html.parser")

    date_lst = list(soup.find("h4"))

    date_str = date_lst[0][29:]

    return date_str

def write_csv():

    url = 'http://88.45.133.130/meteoambientecampania/php/pubblicazione_dati_centraline_valori_medi.php'


    data_page = requests.get(url)

    soup = BeautifulSoup(data_page.content, "html.parser")

    tables = list(soup.findAll("table"))

    for table_index in range(len(tables)):


        table_data = list(tables[table_index].findAll("tr"))

        stations_data = [list(data.findAll("td")) for data in table_data]



        for i in range(len(stations_data)):
            station_data = stations_data[i]
            for j in range(len(station_data)):
                station_data[j] = station_data[j].text.encode('utf-8')


        
        if table_index == 0:
            table_to_write = "pm10.csv"

        elif table_index == 1:
            table_to_write = "pm2_5.csv"

        elif table_index == 2:
            table_to_write = "no2.csv"

        elif table_index == 3:
            table_to_write = "o3.csv"

        elif table_index == 4:
            table_to_write = "co.csv"

        elif table_index == 5:
            table_to_write = "so2.csv"

        elif table_index == 6:
            table_to_write = "benzene.csv"




        with open("csv/pollution_data/{}".format(table_to_write), 'w') as f:

                writer = csv.writer(f)

                for station_data in stations_data:

                    writer.writerow(station_data)



def calculate_distance(city1, city2):
    delta_lat = math.radians(city1.lat - city2.lat)
    delta_long = math.radians(city1.long - city2.long)
    a = pow(math.sin(delta_lat/2),2) + (math.cos(city1.lat)*math.cos(city2.lat)*pow(math.sin(delta_long/2),2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = 6371 * c
    return d


def get_nearest_loc(c, list):

    distance_dict = {}

    for loc in list:
        d = calculate_distance(c, loc)
        distance_dict.update({loc.name : d})

    sorted_distance = sorted((value, key) for (key,value) in distance_dict.items())

    nl = sorted_distance[0]

    return nl




def get_value(data_file, name):

    data_file = list(data_file)


    for i in range(1,len(data_file)):
        if data_file[i][0]==name:
            return float(data_file[i][4])
        else:
            continue
