import json, random

with open("locations.json") as j:
	data = json.load(j)


def overwrite():
	with open("locations.json", "w") as f:
		json.dump(data, f, indent=4)


def backup():
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


# Assigns a random rating to each location (1-5 stars)
def assignRandomRating():
	for location in data:
		location["rating"] = str(random.randint(1,5))


# Used to separate address and telephone from description
# Only should be used once!
def fixDescription():
	for location in data:
		description = location["description"]
		descriptionSplit = description.split(". ", 2)
		location["address"] = descriptionSplit[0]
		location["telephone"] = descriptionSplit[1]
		location["description"] = descriptionSplit[2]
	overwrite()


# Adds true/false for if the location has free admission
def addPrice():
	for location in data:
		if "free" in location["description"].lower():
			location["free"] = True
		else:
			location["free"] = False


# Uncomment to call functions
# updateTypes()
# updateGroupSizes()
# assignRandomRating()
# updateTownName()
# fixDescription()
# addPrice()
# overwrite()
# backup()
