# Filters data from locations.json based on user input
# Displays filtered data
import json

# Opens data file for filtering
with open("locations.json") as j:
    data = json.load(j)

# Array to be used for filtering
# data contains all information
fltData = data

# Resets fltData
def resetFilter():
    global fltData
    global data
    print(len(fltData))
    fltData = data
    print("Filter reset")
    print(len(fltData))


# Searches through data based on desired attributes
def locationsFilter(type, input, array):
    for location in array:
        if input in location[type]:
            array.append(location) # obv this wont work
        else:
            continue

    return array


