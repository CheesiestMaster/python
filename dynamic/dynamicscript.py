# Dynamic Open Source Python Program

#Import Modules
import requests
from os import getcwd

# User Input
owner = input("Who's Repo should I use (Leave blank for default): ")
if owner == "":
    owner = "CheesiestMaster"
else:
	print("Origin Switched to: "+owner)
	print("I am not responsible for if you download a virus from a non default repository")
project = input("Target program name: ")
while project == "":
    project = input("Target program name: ")

#Networking
url = "http://raw.github.com/"+owner+"/python/main/dynamic/"+project+".py"
r=requests.get(url)

#File Manipulation
directory = getcwd()
filename = directory + "/dynamictmp.py"
f=open(filename, 'w')
f.write(r.text)
f.close()

# Execute temporary file
import dynamictmp
