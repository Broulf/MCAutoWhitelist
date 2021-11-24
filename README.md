# Minecraft Auto Whitelist
Takes a list of MC USernames and creates a proper whitelist.json file

# NOTE
If the program is not running correctly / not creating the whitelist.json file, 
uncomment the _print(api_requests.text)_ line, it will print each name and UUID in console
until it gets to a name that is not valid. Only real usernames will allow this program to work, otherwise, it will not.

# Usage
To use this program 
1. Put the whitelist.py file in the same dir as a .txt file named: names.txt (names2.txt is an example of how the names.txt file should be)
2. Run the python program
3. (Optional) Beautify the whitelist.json file online, OR in VScode by opening it and hitting _SHIFT+ALT+F_
