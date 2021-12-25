import json, random

with open("locations.json") as j:
	data = json.load(j)

# open("locations2.json", "x")

def overwrite():
	with open("locations2.json", "w") as f:
		json.dump(data, f, indent=4)

# Adding types to data
def updateTypes():
	for location in data:
		if "park" in location["name"].lower():
			location["type"] = "park"
			continue
		# Manual selection of type
		if location["type"] == "":
			print(location["name"])
			print(location["description"])
			choice = int(input("1-Nature 2-Theme Park 3-Other"))
			if choice == 1:
				location["type"] = "nature"
			elif choice == 2:
				location["type"] = "theme park"
			elif choice == 3:
				location["type"] = "other"
			overwrite()


# Adding group sizes to data
def updateGroupSizes():
	for location in data:
		if location["type"] == "museum":
			location["group size"] = "duo"
		elif location["type"] == "park":
			location["group size"] = "duo"
		elif location["type"] == "nature":
			location["group size"] = "solo"
		elif location["type"] == "theme park":
			location["group size"] = "family"
		# Manual selection of size
		elif location["type"] == "other":
			print(location["name"])
			print(location["description"])
			choice = int(input("1-Solo 2-Duo 3-Family"))
			if choice == 1:
				location["group size"] = "solo"
			if choice == 2:
				location["group size"] = "duo"
			if choice == 3:
				location["group size"] = "family"
	overwrite()

# Assigns a random rating to each location (1-5 stars)
def assignRandomRating():
	for location in data:
		location["rating"] = str(random.randint(1,5))
	overwrite()

def updateTownName():
	for location in data:
		location["town"] = ""
	overwrite()

# overwrite() # use to update backup file
# updateTypes()
# updateGroupSizes()
# assignRandomRating()
# updateTownName()
