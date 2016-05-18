class Number():
	def __init__(self, number):
		self.__num = number

	def get_value(self):
		return self.__num

	def set_value(self, value):
		self.__num = value

	def __cmp__(self, other):
		if self.__num == other.__num:
			return True
		return False

	def __nonzero__(self):
		if self.__num == 0:
			return False
		return True

	def __add__(self, other):
		return Number(self.get_value() + other.get_value())

	def __sub__(self, other):
		return Number(self.get_value() - other.get_value())

	def __mul__(self, other):
		return Number(self.get_value() * other.get_value())

	def __div__(self, other):
		return Number(int(self.get_value() / other.get_value()))

	def __str__(self):
		return str(self.get_value())


if __name__ == "__main__":
	n4 = Number(4)
	n5 = Number(5)
	n1 = Number(1)

	n1.set_value(n4 + n5)
	print n1
