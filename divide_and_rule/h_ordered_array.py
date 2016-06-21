from threading import Thread, Lock, active_count, enumerate
import sys

lock = Lock()
class OrderedArrayThread(Thread):
	count = 0
	list = []

	def __init__(self, value):
		self.value = value
		Thread.__init__(self)

	def run(self):
		with lock:
			OrderedArrayThread.list += [self.value]
			OrderedArrayThread.list.sort()

class OrderedArray:
	def __init__(self):
		pass

	def add(self, i):
		if not isinstance(i, int):
			raise Exception("number is not an integer")
		thread = OrderedArrayThread(i)
		thread.start()

	def isSorting(self):
		if active_count() == 1:
			return False
		return True

	def __str__(self):
		with lock:
			return str(OrderedArrayThread.list)
