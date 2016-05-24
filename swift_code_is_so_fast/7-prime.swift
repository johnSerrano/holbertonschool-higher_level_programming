func is_prime(number: Int) -> (Bool) {
	for i in 2..<number {
		if number % i == 0 {
			return false
		}
	}
	return true
}

//if is_prime(11) {
//    print("11 is prime")
//}
//if is_prime(20) {
//    print("20 is prime")
//}
