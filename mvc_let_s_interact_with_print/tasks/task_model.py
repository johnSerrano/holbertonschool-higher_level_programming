import json

filename = "tasks.json"

class TaskModel():
	def __init__(self, title):
		if not title or type(title) != str:
			raise Exception("title is not a string")

		self.__title = title
		self.__callback_title = lambda x: None
		self.tasks = []
		try:
			with open(filename, 'r') as f:
				self.deserialize_tasks()
		except:
			pass

	def set_callback_title(self, callback_title):
		self.__callback_title = callback_title

	def add_task(self, task):
		self.tasks.append(task)

	def delete_task(self, index):
		del self.tasks[index]

	def serialize_tasks(self):
		with open(filename, 'w') as f:
			f.write(json.dumps(self.tasks))

	def deserialize_tasks(self):
		with open(filename, 'r') as f:
			self.tasks = json.load(f)

	def get_title(self):
		return self.__title

	def toggle(self):
		self.__title = self.__title[::-1]
		self.__callback_title()



if __name__ == "__main__":
	def cb():
		print "AAAAA"

	tm = TaskModel("Title")
	tm.add_task("TASK1")
	tm.add_task("TASK2")
	tm.add_task("TASK3")
	tm.serialize_tasks()
	tm.deserialize_tasks()
	print tm.tasks
	tm.delete_task(1)
	print tm.tasks
