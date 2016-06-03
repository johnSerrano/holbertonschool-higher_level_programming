import json
import xml.dom.minidom
from xml.dom.minidom import Node, Document

class Car:
	def __init__(self, *args, **kwargs):
		if len(args) > 0:
			if isinstance(args[0], dict):
				init_dict = args[0]
			elif isinstance(args[0], str):
				values = args[0].split(',')
				if len(values) == 3:
					init_dict = {"name": values[0], "brand": values[1], "nb_doors": int(values[2])}
		else:
			init_dict = kwargs
		if 'name' not in init_dict.keys() or not (isinstance(init_dict['name'], str) or isinstance(init_dict['name'], unicode)):
			raise Exception('name is not a string')
		if 'brand' not in init_dict.keys() or not (isinstance(init_dict['brand'], str) or isinstance(init_dict['brand'], unicode)):
			raise Exception('brand is not a string')
		if 'nb_doors' not in init_dict.keys() or not (isinstance(init_dict['nb_doors'], int) or isinstance(init_dict['nb_doors'], unicode)) or init_dict['nb_doors'] <= 0:
			raise Exception('nb_doors is not > 0')
		self.__name = init_dict['name']
		self.__brand = init_dict['brand']
		self.__nb_doors = init_dict['nb_doors']

	def get_name(self):
		return self.__name

	def get_brand(self):
		return self.__brand

	def get_nb_doors(self):
		return self.__nb_doors

	def set_nb_doors(self, nb_doors):
		self.__nb_doors = nb_doors

	def to_hash(self):
		return {
			"name": self.__name,
			"brand": self.__brand,
			"nb_doors": self.__nb_doors,
		}

	def to_json_string(self):
		return json.dumps(self.to_hash())

	def __str__(self):
		return self.__name + " " + self.__brand + " (" + str(self.__nb_doors) + ")"

	def to_comma(self):
		return self.__name + "," + self.__brand + "," + str(self.__nb_doors) + "\n"

	def to_xml_node(self, doc, root="car"):
		# just use the json, seriously
		d = self.to_hash()
		op = lambda tag: '<' + tag + '>'
		cl = lambda tag: '</' + tag + '>\n'
		ml = lambda v,xmlstr,key: xmlstr + op(key) + str(v) + cl(key)

		xmlstr = '<' + root + ' nb_doors="' + str(d['nb_doors']) + '">' + '\n' if root else ""

		xmlstr = xmlstr + op('name') + '<![CDATA[' + d['name'] + ']]>' + cl('name')
		xmlstr = ml(d['brand'],xmlstr,"brand")

		xmlstr += cl(root) if root else ""

		for node in xml.dom.minidom.parseString(xmlstr).getElementsByTagName(root):
			return node

	@staticmethod
	def load_from_hash(car):
		return Car(name=car['name'], brand=car['brand'], nb_doors=car['nb_doors'])

if __name__ == "__main__":
	with open("5-main.json") as f:
		cars_json_list = json.loads(f.read())
	cars = []
	for car in cars_json_list:
		cars.append(Car(car))
	brands = []
	total_doors = 0
	xmlstr = '<cars>\n</cars>\n'
	doc = xml.dom.minidom.parseString(xmlstr)
	for i, car in enumerate(cars):
		doc.getElementsByTagName('cars')[0].appendChild(car.to_xml_node(doc))
		total_doors += car.get_nb_doors()
		if car.get_brand() not in brands:
			brands.append(car.get_brand())
	print len(brands)
	print total_doors
	if cars[3]: print cars[3]
	print doc.toxml(encoding='utf-8')


	# c = Car(name="Rogue", brand="Nissan", nb_doors=5)
	# print c
	# c_json_string = c.to_json_string()
	# print type(c_json_string)
	# print c_json_string
	#
	# doc = Document()
	# c_xml = c.to_xml_node(doc)
	# doc.appendChild(c_xml)
	# print doc.toxml(encoding='utf-8')
