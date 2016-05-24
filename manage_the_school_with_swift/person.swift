class Person {
  var first_name: String
  var last_name: String
  var age: Int

  init(first_name: String, last_name: String, age: Int) {
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
  }

  func fullName() -> String {
    return self.first_name + " " + self.last_name
  }
}

// var p = Person(first_name: "John", last_name: "Fring", age: 30)
//
// print("name: \(p.first_name)")
// print("fullName: \(p.fullName())")
