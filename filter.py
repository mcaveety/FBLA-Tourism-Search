# Filters data from locations.json based on user input
# Displays filtered data
import json

# Opens data file for filtering
with open("locations.json") as j:
    data = json.load(j)

# Searches through data based on desired attributes
def locationsFilter(type, input, list):
    for location in list:
        if input in location[type]:
            yield location

    return list

def displayTypes(fltList, types):
    length = sum(1 for location in fltList)
    if length == len(data):
        string = "Displaying all location entries"
    elif 0 < length < len(data):
        string = "Displaying entries filtered by " + types
    elif length == 0:
        string = "No matching location entries for selected filters"

    return string # dont want it to stop program tho :(
