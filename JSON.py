#JAVA script object notatio
#client & server
# python JSON linbrary
import json
print(dir(json))
#load S F
#Dump S dump F
json_file_dir = "dir"
movies = json.load(json_file_dir)
json_file_dir.close()

import xml.etree.ElementTree as ET

from inspect import getmembers, isclass


# display  classes in ET module

for (name, member) in getmembers(ET, isfunction):
    if not name.startswith("_"):
        print(name)
# XM:L I WILL FOCUS ON ELEMENT & ELEMENT TREE
# XML IS data structure Node has single
#xml tree  is eah node node = elememt = elemet = tags starts stag and end tag <user> </user>
#uuser is an elenent can have tag elements
# element is pair of tag <user> </usewr> element can coniatan atrrbityre id attrebute e.g. id + key value datat
# elememgt e.eg user can contain text between the tags and even otehr elemne5bns

import xml.etree.ElementTree as ET

from inspect import getmembers, isclass


# display  classes in ET module

for (name, member) in getmembers(ET, isfunction):
    if not name.startswith("_"):
        print(name)
# XM:L I WILL FOCUS ON ELEMENT & ELEMENT TREE
# XML IS data structure Node has single
#xml tree  is eah node node = elememt = elemet = tags starts stag and end tag <user> </user>
#uuser is an elenent can have tag elements
# element is pair of tag <user> </usewr> element can coniatan atrrbityre id attrebute e.g. id + key value datat
# elememgt e.eg user can contain text between the tags and even otehr elemne5bns

