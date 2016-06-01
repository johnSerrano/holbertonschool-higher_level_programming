import xml.etree.ElementTree
import sys

filename = "1.xml"

if (len(sys.argv) > 1):
    filename = int(sys.argv[1])

e = xml.etree.ElementTree.parse(filename).getroot()

for child in e:
	#products
	for catalog in child:
		#catalogs
		# if catalog.get("gender") != "Women's":
		# 	continue
		for size in catalog.findall('size'):
			# print size.tag, size.attrib
			for color in size.findall('color_swatch'):
				print color.tag, color.attrib
