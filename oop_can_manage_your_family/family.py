import json

class Person():
	EYES_COLORS = ["Blue", "Green", "Brown"]
	GENRES = ["Female", "Male"]
	def __init__(self, id, first_name, date_of_birth, genre, eyes_color, is_married_to=0, last_name=None, children=[]):
		if id < 0 or type(id) != int:
			raise Exception("id is not an integer")
		if not first_name or type(first_name) != str:
			raise Exception("string is not a string")
		if type(date_of_birth) != list or len(date_of_birth) != 3 or not all(isinstance(x, int) for x in date_of_birth):
			raise Exception("date_of_birth is not a valid date")
		if genre not in Person.GENRES:
			raise Exception("genre is not valid")
		if eyes_color not in Person.EYES_COLORS:
			raise Exception("eyes_color is not valid")

		self.__id = id
		self.__eyes_color = eyes_color
		self.__genre = genre
		self.__gender = genre
		self.__date_of_birth = date_of_birth
		self.__first_name = first_name
		self.last_name = last_name
		self.is_married_to = is_married_to
		self.children = children[:]

#untested
	@staticmethod
	def load_from_json(json):
		if not type(json) == dict:
			raise Exception("json is not valid")
		if not all(i in json.keys() for i in ["id", "eyes_color", "genre", "date_of_birth", "first_name", "last_name", "is_married_to", "children"]):
			raise Exception("JSON missing fields")
		if "type" in json.keys():
			try:
				return {"Baby": Baby,
				"Teenager": Teenager,
				"Adult": Adult,
				"Senior": Senior,
			 	}[json["type"]](json["id"],
								str(json["first_name"]),
								json["date_of_birth"],
								json["genre"],
								json["eyes_color"],
								json["is_married_to"],
								str(json["last_name"]),
								json["children"])
			except:
				pass
		#default return person
		return Person(json["id"],
					  str(json["first_name"]),
					  json["date_of_birth"],
					  json["genre"],
					  json["eyes_color"],
					  json["is_married_to"],
					  str(json["last_name"]),
					  json["children"])

	def json(self):
		return {
			"type": self.type_string(),
			"id": self.__id,
			"eyes_color": self.__eyes_color,
			"genre": self.__genre,
			"date_of_birth": self.__date_of_birth,
			"first_name": self.__first_name,
			"last_name": self.last_name,
			"is_married_to": self.is_married_to,
			"children": self.children
		}

	def __str__(self):
		str = self.__first_name
		if self.last_name:
			str += " " + self.last_name
		return str

	def __repr__(self):
		return self.__str__()

	def get_id(self):
		return self.__id

	def is_married(self):
		if self.is_married_to:
			return True
		return False

	def divorce(self, p):
		if not self.__id == p.is_married_to or not p.__id == self.is_married_to:
			raise Exception("Not married to each other")
		self.is_married_to = 0
		p.is_married_to = 0

	def just_married_with(self, p):
		if p.is_married() or self.is_married():
			raise Exception("Already married")
		if not p.can_be_married() or not self.can_be_married():
			raise Exception("Can't be married")
		self.is_married_to = p.__id
		p.is_married_to = self.__id
		if {self.__gender, p.__gender} == {"Male", "Female"}:
			if p.__gender == "Male" and p.last_name:
				self.last_name = p.last_name
			elif self.__gender == "Male" and self.last_name:
				p.last_name = self.last_name

	def can_be_married(self):
		return any(isinstance(self, kind) for kind in [Adult, Senior])

	def type_string(self):
		return "Person"

	def is_male(self):
		return self.__gender == "Male"

	def age(self):
		age_ = 2016 - self.__date_of_birth[2]
		if self.__date_of_birth[0] >= 5 and self.__date_of_birth[1] >= 20:
			age_ += 1
		return age_

	def can_have_child(self):
		# return isinstance(self, Adult)
		return True

	def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color=None, married_to=0, last_name=None):
		if not all(person.can_have_child() for person in [self, p]):
			raise Exception("Can't have baby")
		if not eyes_color:
			if any(color == "Brown" for color in [self.__eyes_color, p.__eyes_color]):
				eyes_color = "Brown"
			elif any(color == "Blue" for color in [self.__eyes_color, p.__eyes_color]):
				eyes_color = "Blue"
			else:
				eyes_color = "Green"
		baby = Baby(id, first_name, date_of_birth, genre, eyes_color, married_to, last_name)
		self.children.append(id)
		p.children.append(id)
		return baby

	def get_eyes_color(self):
		return self.__eyes_color

	def adopt_child(self, c):
		if not self.can_have_child():
			raise Exception("Can't adopt child")
		self.children.append(c.__id)

	def who_are_my_grandchildren(self, list_person):
		raise NotImplementedError("Please Implement this method")

	def who_are_my_grand_parents(self, list_person):
		raise NotImplementedError("Please Implement this method")

	def who_are_my_parents(self, list_person):
		raise NotImplementedError("Please Implement this method")

	def can_run(self):
		raise NotImplementedError("Please Implement this method")

	def need_help(self):
		raise NotImplementedError("Please Implement this method")

	def is_young(self):
		raise NotImplementedError("Please Implement this method")

	def can_vote(self):
		raise NotImplementedError("Please Implement this method")

	def __cmp__(self, other):
		if self.age() == other.age():
			return True
		return False

	def __lt__(self, other):
		if self.age() < other.age():
			return True
		return False

	def __le__(self, other):
		if self.age() <= other.age():
			return True
		return False

	def __ne__(self, other):
		if self.age() != other.age():
			return True
		return False

	def __gt__(self, other):
		if self.age() > other.age():
			return True
		return False

	def __ge__(self, other):
		if self.age() >= other.age():
			return True
		return False


class Baby(Person):
	def can_run(self):
		return False

	def need_help(self):
		return True

	def is_young(self):
		return True

	def can_vote(self):
		return False

	def type_string(self):
		return "Baby"

	def who_are_my_parents(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")
		return [person for person in list_person if self.get_id() in person.children]

	def who_are_my_grand_parents(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")
		return [person for sublist in [grandparent for grandparent in [parent.who_are_my_parents(list_person) for parent in self.who_are_my_parents(list_person)]] for person in sublist]


class Teenager(Person):
	def can_run(self):
		return True

	def need_help(self):
		return False

	def is_young(self):
		return True

	def can_vote(self):
		return False

	def type_string(self):
		return "Teenager"

	def who_are_my_parents(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")
		return [person for person in list_person if self.get_id() in person.children]

	def who_are_my_grand_parents(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")
		return [person for sublist in [grandparent for grandparent in [parent.who_are_my_parents(list_person) for parent in self.who_are_my_parents(list_person)]] for person in sublist]


class Adult(Person):
	def can_run(self):
		return True

	def need_help(self):
		return False

	def is_young(self):
		return False

	def can_vote(self):
		return True

	def type_string(self):
		return "Adult"

	def who_are_my_parents(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")
		return [person for person in list_person if self.get_id() in person.children]

	def who_are_my_grand_parents(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")
		return [person for sublist in [grandparent for grandparent in [parent.who_are_my_parents(list_person) for parent in self.who_are_my_parents(list_person)]] for person in sublist]


class Senior(Person):
	def can_run(self):
		return False

	def need_help(self):
		return True

	def is_young(self):
		return False

	def can_vote(self):
		return True

	def type_string(self):
		return "Senior"

	def who_are_my_grandchildren(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")
		return [grandchild for grandchild in list_person if grandchild.get_id() in [person for sublist in [child.children for child in [person for person in list_person if person.get_id() in self.children]] for person in sublist]]


def save_to_file(list, filename="family.json"):
	with open(filename, "w") as f:
		f.write(json.dumps([i.json() for i in list]))

def load_from_file(filename="family.json"):
	try:
		with open(filename, "r") as f:
			jsons = json.load(f)
	except:
		raise Exception("filename is not valid or doesn't exist")
	return [Person.load_from_json(json_hash) for json_hash in jsons]

if __name__ == "__main__":
	family = [Adult(1, "Monica", [5, 6, 1993], "Female", "Green", 0, "Lewinski"),
			  Senior(2, "Bill", [5, 7, 1993], "Male", "Blue", 0, "Clinton"),
			  Adult(3, "Anne", [5, 7, 1993], "Male", "Blue", 0, "Annatoli"),
			  Adult(4, "Aaron", [5, 7, 1993], "Male", "Blue", 0, "Andrews")]
	monica = family[0]
	bill = family[1]
	anne = family[2]
	aaron = family[3]

	bill.just_married_with(monica)

	hillary = bill.has_child_with(monica, 5, "Hillary", [1, 1, 1999], "Female", None, 0, "Clinton")
	alex = aaron.has_child_with(anne, 6, "Alexander", [1, 1, 1999], "Male", None, 0, "Andrews")

	# should fail (can't have baby exception) change for debug purposes
	amelie = alex.has_child_with(hillary, 7, "Amelie", [1, 1, 1999], "Male", None, 0, "Andrews")

	family.append(hillary)
	family.append(alex)
	family.append(amelie)

	save_to_file(family, "family.json")
	family = load_from_file("family.json")

	monica = family[0]
	bill = family[1]
	anne = family[2]
	aaron = family[3]
	hillary = family[4]
	alex = family[5]

	print amelie.who_are_my_grand_parents(family)
	print bill.who_are_my_grandchildren(family)
