import json

with open("data.json", "r") as f:
    data = json.load(f)
    print(data)

#Modify data (Example: add a new key)
data["status"] = "Process"
data["Address"] = "New Delhi"

#delete
if "status" in data:
    del data["status"]

#Write to a new JSON file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
print("\nUpdated JSON saved!")    



