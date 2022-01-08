# Filters data from locations.json based on user input
# Yields a generator containing matching locations

import json, os, sys

# Allows data to be accessed after PyInstaller bundles the program up
# Code credit: https://stackoverflow.com/a/13790741
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Opens data file for filtering
with open(resource_path("json/locations.json")) as j:
    data = json.load(j)

# Backs up data to a second file
def backup():
    with open(resource_path("json/locations2.json"), "w") as f:
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

