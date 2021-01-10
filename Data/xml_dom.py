from xml.dom import minidom
import random
import string

data = minidom.parse('C:\\Users\\Admin\\source\\repos\\hello_world\\hello_world\\Data\\example.xml')

cNodes = data.childNodes
itemList = data.getElementsByTagName('item')

for i in cNodes[0].getElementsByTagName("osoba"):
	print(i.getElementsByTagName("imie")[0].nodeName)
	print(i.getElementsByTagName("imie")[0].childNodes[0].toxml())
	print(i.getElementsByTagName("imie")[0].getAttribute("foo"))

for index, item in enumerate(itemList):
    itemList[index].attributes["name"].value = "name123"

with open("C:\\Users\\Admin\\source\\repos\\hello_world\\hello_world\\Data\\mod_example.xml", "w") as new_data:
    data.writexml(new_data)