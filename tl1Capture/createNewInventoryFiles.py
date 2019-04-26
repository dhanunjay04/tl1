"""
Created on Mon Apr  26 13:30:54 2019

@author: Dhana Varakala
"""

import xml.etree.ElementTree as ET

def getInventorys(file):
    id = []
    type = ET.parse(file)
    root = type.getroot()
    for point in root.findall('./point-type'):
        id.append(point.attrib)

    return id
def main():

       print(getInventorys('/home/dhanu/workspace/vsure/centina/sa/profiles/tl1/inventory/fujitsu-flashwave-4100es.xml'))


if __name__ == "__main__":
    main()
