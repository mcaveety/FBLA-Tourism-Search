# Filters data from locations.json based on user input
# Returns a list
import json
from flask import url_for

# Opens data file for filtering
with open("static/locations.json") as j:
    data = json.load(j)

# Searches through data based on user inputs gathered from POST request
def locationsFilter(type, input, list):
    for location in list:
        if input.lower() in location[type].lower():
            yield location

