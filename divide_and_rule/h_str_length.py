from threading import Thread, Lock
strlock = Lock()

class StrLengthThread(Thread):
	total_str_length = 0;

	def __init__(self, word):
		self.word = word
		if not isinstance(word, str):
			raise Exception("word is not a string")
		Thread.__init__(self)

	@staticmethod
	def update_total_length(value):
		with strlock:
			StrLengthThread.total_str_length += value

	def run(self):
		self.update_total_length(len(self.word))
