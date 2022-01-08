# Filters data from locations.json based on user input
# Yields a generator containing matching locations

import json

# Opens data file for filtering
with open("json/locations.json") as j:
    data = json.load(j)

# Backs up data to a second file
def backup():
    with open("json/locations2.json", "w") as f:
        json.dump(data, f, indent=4)


"""
Searches through data based on user inputs gathered from POST request
If multiple types are selected, the filter is run multiple times
Each time, the data is filtered by one of the selected types
The filtered generator is then iterated through again and filtered further
"""
def locationsFilter(type, input, list):
    for location in list:
        if input.lower() in location[type].lower():
            yield location

