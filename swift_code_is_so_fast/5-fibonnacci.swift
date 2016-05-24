func fibonacci(number: Int) -> (Int) {
	var slow = 1, fast = 1, count = 2
	while count < number {
		(slow, fast) = (fast, slow+fast)
		count += 1
	}
	return fast
}

//print("Fibonnacci of 3 is \(fibonacci(3))")
//print("Fibonnacci of 7 is \(fibonacci(7))")
//print("Fibonnacci of 18 is \(fibonacci(18))")
