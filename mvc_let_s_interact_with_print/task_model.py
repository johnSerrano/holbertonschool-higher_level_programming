class TaskModel():
	def __init__(self, title):
		if not title or type(title) != str:
			raise Exception("title is not a string")
		self.__title = title
		self.__callback_title = lambda x: None

	def set_callback_title(self, callback_title):
		self.__callback_title = callback_title

	def get_title(self):
		return self.__title

	def toggle(self):
		self.__title = self.__title[::-1]
		self.__callback_title()



if __name__ == "__main__":
	def cb():
		print "AAAAA"

	tm = TaskModel("Title")
	tm.set_callback_title(cb)
	print tm.get_title()
	tm.toggle()
	print tm.get_title()
