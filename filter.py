# Filters data from locations.json based on user input
import json

# Opens data file for filtering
with open("locations.json") as j:
    data = json.load(j)

# Array to be used for filtering
# data contains all information
fltData = data

# Resets fltData
def resetFilter(filter):
    filter = data
    print("Filter reset")
    return filter

# Searches through data based on desired attributes
def filterType(type, input):
    print("Type: " + type)
    print("Input: " + input)
    if type == "name":
        locationsFilter(type, input, fltData)
    elif type == "type":
        locationsFilter(type, input, fltData)
    elif type == "price":
        locationsFilter(type, input, fltData)
    elif type == "group size":
        locationsFilter(type, input, fltData)
    elif type == "rating":
        locationsFilter(type, input, fltData)

def locationsFilter(type, input, array):
    for location in array:
        if input in location[type]:
            print(location)



