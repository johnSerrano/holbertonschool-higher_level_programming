func is_palindrome(s: String) -> Bool {
  return s.characters.reverse().map {String($0)}.joinWithSeparator("") == s
}
