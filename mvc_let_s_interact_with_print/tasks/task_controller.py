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

	def title_callback(self):
		# callback should run update_title from view with model.title
		self.__view.update_title(self.__model.get_title())

if __name__ == '__main__':
	root = tk.Tk()
	# root.withdraw()
	t = TaskModel("Finish this funny project")
	tc = TaskController(root, t)
	root.mainloop()
