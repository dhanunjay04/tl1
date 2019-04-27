"""
Created on Mon Apr  26 13:30:54 2019

@author: Dhana Varakala
"""

import xml.etree.ElementTree as ET

def getInventorys(file):
    id = []
    type = ET.parse(file)
    getroot = type.getroot()
    root = getroot
    for point in root.findall('./point-type'):
        id.append(point.attrib)

    return id
def main():

       data = getInventorys('fujitsu-flashwave-4100es.xml')
       i = 0
       for index in data:
           i = i+1
           print(i,"  ", index["name"])
       length = data.__len__()
       print(length)


if __name__ == "__main__":
    main()
