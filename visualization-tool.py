import csv
from vector import placevector

filename = input("Location of csv file to pull data from?\n")

with open(filename, 'r') as rawdata:
    reader = csv.reader(rawdata, delimiter=',')
    i = 0
    for row in reader:
        placevector(i, row)
        print(row)
        i = i+1

with open('vector.csv', 'r') as vectors:
    vecReader = csv.reader(vectors, delimiter=',')
    for row in vecReader:
        print(row)
