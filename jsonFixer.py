import json

with open("locations.json") as j:
	data = json.load(j)

def overwrite():
	with open("locations.json", "w") as f:
		json.dump(data, f, indent=4)

# Adding types to data
for location in data:
	if "park" in location["name"].lower():
		location["type"] = "park"
		continue
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

