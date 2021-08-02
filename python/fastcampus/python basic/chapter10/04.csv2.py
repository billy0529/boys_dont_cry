import csv
from os import read
file = open("billy.pickle")
reader = csv.reader(file)
for data in reader:
    print(data)

file.close()
