# Anthony Segura
# Reads a .TXT file and outputs a list of names and UUIDS into a whitelist.json file

import requests
import json
import uuid
import os

def main():
    # Opens the TXT that contains the names
    names_list = open("names.txt", "r")
    
    # Storage for dictionary
    whitelist = []
    
    for line in names_list:
        # Creates and API requests for each name and strips the names and UUIDs
        api_request = requests.get("https://api.mojang.com/users/profiles/minecraft/" + line.rstrip())
        #print(api_request.status_code)
        #print(api_request.text)
    
        # If the API request is successful, add the name and UUID to the dictionary
        if api_request.status_code == 200:
            load_json = json.loads(api_request.text)
            whitelist.append({
                "uuid": str(uuid.UUID(load_json['id'])),
                "name": load_json['name']
            })
    
    # Writes the dictionary with the help of os to pipe it into whitelist.json
    print(json.dumps(whitelist))
    os.system("python whitelist.py > whitelist.json")

main()
