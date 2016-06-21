from threading import Thread

class FibonacciThread(Thread):
	def __init__(self, i):
		if not isinstance(i, int):
			raise Exception("number is not an integer")
		self.i = i
		Thread.__init__(self)

	def run(self):
		one = 0;
		two = 1;

		for j in range(self.i):
			(one, two) = (two, one + two)

		print str(self.i) + " => " + str(one);
