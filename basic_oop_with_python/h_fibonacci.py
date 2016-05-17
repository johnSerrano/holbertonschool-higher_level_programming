def fibonacci(index):
	fib = [1, 1]
	while len(fib) < index:
		fib.append(fib[-1] + fib[-2])
	return fib[index-1]

if __name__ == "__main__":
	for i in range(1, 20):
	    print "Fibonacci of %d is %d" % (i, fibonacci(i))
