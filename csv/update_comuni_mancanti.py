import csv

file_1 = csv.reader(open("comuni_mancanti_coord7.csv",'r'))
file_2 = csv.reader(open("comuni_mancanti_coord6.csv",'r'))
file_3 = csv.reader(open("comuni_mancanti_coord5.csv",'r'))
file_4 = csv.reader(open("comuni_mancanti_coord4.csv",'r'))
file_5 = csv.reader(open("comuni_mancanti_coord3.csv",'r'))
file_6 = csv.reader(open("comuni_mancanti_coord2.csv",'r'))
file_7= csv.reader(open("comuni_mancanti_coord.csv",'r'))
file_8 = csv.reader(open("comuni_coordinate.csv",'r'))


d_1 = list(file_1)
d_2 =list(file_2)
d_3 = list(file_3)
d_4 = list(file_4)
d_5 = list(file_5)
d_6 = list(file_6)
d_7 = list(file_7)
d_8 = list(file_8)





for data_1 in d_1:
    for data_2 in d_2:
        if data_1[0] == data_2[0]:
            del data_2[-1]
            data_2.append(data_1[1])
            data_2.append(data_1[2])

for data_2 in d_2:
    for data_3 in d_3:
        if data_2[0] == data_3[0]:
            del data_3[-1]
            data_3.append(data_2[1])
            data_3.append(data_2[2])

for data_3 in d_3:
    for data_4 in d_4:
        if data_3[0] == data_4[0]:
            del data_4[-1]
            data_4.append(data_3[1])
            data_4.append(data_3[2])

for data_4 in d_4:
    for data_5 in d_5:
        if data_4[0] == data_5[0]:
            del data_5[-1]
            data_5.append(data_4[1])
            data_5.append(data_4[2])

for data_5 in d_5:
    for data_6 in d_6:
        if data_5[0] == data_6[0]:
            del data_6[-1]
            data_6.append(data_5[1])
            data_6.append(data_5[2])

for data_6 in d_6:
    for data_7 in d_7:
        if data_6[0] == data_7[0]:
            del data_7[-1]
            data_7.append(data_6[1])
            data_7.append(data_6[2])

for data_7 in d_7:
    for data_8 in d_8:
        if data_7[0] == data_8[0]:
            del data_8[-1]
            data_8.append(data_7[1])
            data_8.append(data_7[2])





with open("COMUNI_COORDINATE_1.csv",'w') as f:
    writer = csv.writer(f)
    for row in d_8:
        writer.writerow(row)