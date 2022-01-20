# Dynamic Open Source Python Program

#Prevent Nesting of the file
if __file__.rsplit("/", 1)[1].split('.')[0] == 'dynamictmp':
    print("Nice Try but you can't do that")
    quit()

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
