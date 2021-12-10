# 10.12.2021
# Filters data from locations.csv based on user input

import csv

f = open('locations.csv')

with open('locations.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

f.close()