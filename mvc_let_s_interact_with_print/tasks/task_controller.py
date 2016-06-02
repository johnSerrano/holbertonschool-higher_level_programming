import Tkinter as tk
from task_model import TaskModel
from task_view import TaskView

class TaskController():
	def __init__(self, master, model):
		if not master or not isinstance(master, tk.Tk):
			raise Exception("master is not a tk.Tk()")

		self.__view = TaskView(master)
		self.__model = model

		self.__model.set_callback_title(self.title_callback)
		self.__view.update_title(self.__model.get_title())
		self.__view.toggle_button.config(command=self.__model.toggle)

		self.__view.delete_button.config(command=self.task_delete)
		self.__view.add_button.config(command=self.task_add)

		for item in self.__model.tasks:
			self.__view.listbox.insert(tk.END, item)

	def task_add(self):
		task = self.__view.entry.get()
		self.__view.listbox.insert(tk.END, task)
		self.__model.add_task(task)

	def task_delete(self):
		indexes = list(self.__view.listbox.curselection())
		indexes.sort(reverse=True)
		for index in indexes:
			self.__model.delete_task(index)
			self.__view.listbox.delete(index)

	def title_callback(self):
		# callback should run update_title from view with model.title
		self.__view.update_title(self.__model.get_title())

if __name__ == '__main__':
	root = tk.Tk()
	# root.withdraw()
	t = TaskModel("Finish this funny project")
	tc = TaskController(root, t)
	root.mainloop()
