func longest_word(s: String) -> String {
  func longer_word(s: String, _ d: String) -> String {
    if s.characters.count > d.characters.count {
      return s
    }
    return d
  }
  let words = s.characters.split(" ").map(String.init)
  let string = ""
  return words.reduce(string, combine:{longer_word($0, $1)})
}

var my_text = "I don't know which word will be the longest of this sentence, so I will try to find it!"
print("\"\(longest_word(my_text))\" is the longest word in \"\(my_text)\"")
