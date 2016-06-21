from threading import Thread, Lock
strlock = Lock()

class ReverseStrThread(Thread):
	sentence = ""
	blobs = []
	count = 0

	def __init__(self, word):
		if not isinstance(word, str):
			raise Exception("word is not a string")
		self.word = word
		self.id = ReverseStrThread.count
		ReverseStrThread.count += 1
		Thread.__init__(self)

	@staticmethod
	def update_sentence(value, tid):
		with strlock:
			ReverseStrThread.blobs += [(tid, value)]
			ReverseStrThread.blobs.sort(key=lambda x: x[0])
			ReverseStrThread.sentence = ""
			for blob in ReverseStrThread.blobs:
				ReverseStrThread.sentence += blob[1] + " "

	def run(self):
		self.update_sentence(self.word[::-1], self.id)
