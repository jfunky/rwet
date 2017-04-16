#code to create a dictionary from csv
#from https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file

import csv

with open('coors.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    for rows in reader:
        k = rows[0]
        v = rows[1]
        mydict = {k:v for k, v in rows}
    print(mydict)
