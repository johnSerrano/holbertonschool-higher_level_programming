let strings = ["We", "Heart", "Swift"]

let string = { (strings: [String]) -> String in
	var str = ""
	for s in strings {
		if str != "" {
			str += " "
		}
		str += s
	}
	return str
}(strings)

print(string)
