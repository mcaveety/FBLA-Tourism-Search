# 12.10.21
# Filters data from locations.csv based on user input

import csv


with open('locations.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
