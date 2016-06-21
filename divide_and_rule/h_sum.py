from threading import Thread, Lock, active_count
import sys

lock = Lock()
class SumThread(Thread):
	def __init__(self, value):
		self.value = value
		Thread.__init__(self)

	def run(self):
		with lock:
			Sum.total += sum(self.value)

class Sum:
	total = 0
	def __init__(self, nb_threads, ints):
		Sum.total = 0
		if not isinstance(nb_threads, int):
			raise Exception("nb_threads is not an integer")
		if not isinstance(ints, list) or not all(isinstance(i, int) for i in ints):
			raise Exception("numbers is not an array of integers")
		chunksize = int(len(ints)/nb_threads)
		for i in range(nb_threads-1):
			thread = SumThread(ints[chunksize*i:chunksize*(i+1)])
			thread.start()
		thread = SumThread(ints[chunksize*(nb_threads-1):])
		thread.start()

	def isComputing(self):
		if active_count() == 1:
			return False
		return True

	def __str__(self):
		with lock:
			return str(Sum.total)
