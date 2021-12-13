# 12.10.21
# Filters data from locations.csv based on user input

import csv

with open('locations.csv') as locations:
    reader = csv.reader(locations)
    for row in reader:
        print(row)

# Displays full list of attractions
def resetFilter():
    # Code here
    print("Search filter reset")

# Searches through data based on desired attributes
def locationsFilter():
    # Code here
    print("Search filtered by: ")


