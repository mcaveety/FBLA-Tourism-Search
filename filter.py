# Filters data from locations.json based on user input
# Returns a list
import json

# Opens data file for filtering
with open("locations.json") as j:
    data = json.load(j)

# Searches through data based on user inputs gathered from POST request
def locationsFilter(type, input, list):
    for location in list:
        if input in location[type]:
            yield location

