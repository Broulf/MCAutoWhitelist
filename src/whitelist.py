# Anthony Segura
# Reads a .TXT file and outputs a list of names and UUIDS into a whitelist.json file

import requests
import json
import uuid
import os

# Opens the TXT that contains the names
names_list = open("names.txt", "r")

# Storage for dictionary
whitelist = []

for line in names_list:
    # Creates and API requests for each name and strips the names and UUIDs
    api_request = requests.get("https://api.mojang.com/users/profiles/minecraft/" + line.rstrip())
    #print(api_request.text)
    load_json = json.loads(api_request.text)

    # Creates a dictionary for each name and UUID
    whitelist.append({
        "uuid": str(uuid.UUID(load_json['id'])),
        "name": load_json['name']
    })

# Writes the dictionary with the help of os to pipe it into whitelist.json
print(json.dumps(whitelist))
os.system("python whitelist.py > whitelist.json")
