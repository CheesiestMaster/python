# Dynamic Open Source Python Program
import requests
from os import getcwd
owner = ""
#owner = input("Who's Repo should I use (Leave blank for default): ")
if owner == "":
    owner = "CheesiestMaster"
else:
	print("Origin Switched to: "+owner)
	print("I am not responsible for if you download a virus from a non default repository")
project = "coterminal-deg"
#project = input("Target program name: ")
while project == "":
    project = input("Target program name: ")
url = "http://raw.github.com/"+owner+"/python/main/dynamic/"+project+".py"
directory = getcwd()
filename = directory + r"/dynamictmp.py"
r=requests.get(url)
import io
f=io.open(filename, 'w', encoding="utf-8")
f.write(r.text)
f.close()
from dynamictmp import code
