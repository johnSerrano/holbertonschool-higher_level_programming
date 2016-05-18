class Square():
	def __init__(self, side_length):
		self.__side_length = side_length
		self.__center = [0, 0]
		self.__color = "black"
		self.name = "square"

	def set_color(self, color):
		self.__color = color

	def set_center(self, center):
		if len(center) == 2:
			self.__center = center

	def area(self):
		return self.__side_length ** 2

	def __call__(self):
		strn = ""
		strn += "".join(["*" for _ in range(0, self.__side_length)]) + "\n"
		for _ in range(2, self.__side_length):
			strn += ("*" + "".join([" " for _ in range(2, self.__side_length)]) + "*\n")
		strn += ("".join(["*" for _ in range(0, self.__side_length)]))
		return strn

if __name__ == "__main__":
	s = Square(4)
	s.set_center([0, 0])
	s.set_color("Yellow")
	s.name = "Hally"
	print("Area of %s is %d" % (s.name, s.area()))
	print s()
