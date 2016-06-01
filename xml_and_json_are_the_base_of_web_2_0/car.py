class Car:
	def __init__(self, *args, **kwargs):
		if 'name' not in kwargs.keys() or not isinstance(kwargs['name'], str):
			raise Exception('name is not a string')
		if 'brand' not in kwargs.keys() or not isinstance(kwargs['brand'], str):
			raise Exception('brand is not a string')
		if 'nb_doors' not in kwargs.keys() or not isinstance(kwargs['nb_doors'], int) or kwargs['nb_doors'] <= 0:
			raise Exception('nb_doors is not > 0')
		self.__name = kwargs['name']
		self.__brand = kwargs['brand']
		self.__nb_doors = kwargs['nb_doors']

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

	def __str__(self):
		return self.__name + " " + self.__brand + " (" + str(self.__nb_doors) + ")"

	@staticmethod
	def load_from_hash(car):
		return Car(name=car['name'], brand=car['brand'], nb_doors=car['nb_doors'])


if __name__ == "__main__":
	car = Car(name="CAAAAR", brand="BRAAAND", nb_doors=3)
	print car.get_name()
	print car.get_brand()
	print car.get_nb_doors()
	print car
	print car.to_hash()
	new_car = Car.load_from_hash(car.to_hash())
	print new_car
