from threading import Thread, Lock
import sys


strlock = Lock()
total_str_length = 0;


class StrLengthThread(Thread):

	def __init__(self, word):
		self.word = word
		if not isinstance(word, str):
			raise Exception("word is not a string")
		Thread.__init__(self)

	@staticmethod
	def update_total_length(value):
		global total_str_length
		with strlock:
			total_str_length += value

	def run(self):
		self.update_total_length(len(self.word))


if len(sys.argv) <= 1:
	raise Exception("Not enough arguments")

text = sys.argv[1]

words = text.split(" ")
str_length_threads = []

total_str_length = len(words)-1
for word in words:
    str_length_thread = StrLengthThread(word)
    str_length_threads += [str_length_thread]
    str_length_thread.start()

for t in str_length_threads:
    t.join()

print total_str_length
