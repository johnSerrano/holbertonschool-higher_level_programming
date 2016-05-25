import Tkinter as tk

class TaskView(tk.Frame):
	def __init__(self, master=None):
		if not master or not isinstance(master, tk.Tk):
			raise Exception("master is not a tk.Tk()")
		self.master = master

		tk.Frame.__init__(self, master)

		self.__title_var = tk.StringVar()
		self.__title_label = tk.Label(master, textvariable=self.__title_var)
		self.__title_label.textvariable = self.__title_var
		self.__title_label.pack(side=tk.RIGHT)

		self.toggle_button = tk.Button(master, text="Reverse")
		self.toggle_button.pack(side=tk.LEFT)

		self.pack()

	def update_title(self, title):
		if not title or not isinstance(title, str):
			raise Exception("title is not a string")
		self.__title_var.set(title)


if __name__ == "__main__":
	root = tk.Tk()
	# root.withdraw()
	tv = TaskView(root)
	tv.update_title("Finish this funny project")
	root.mainloop()
