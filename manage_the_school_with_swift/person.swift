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

protocol Classify {
  func isStudent() -> Bool
}

// var p = Person(first_name: "John", last_name: "Fring", age: 30)
//
// print("name: \(p.first_name)")
// print("fullName: \(p.fullName())")
class Mentor: Person, Classify {
  func isStudent() -> Bool {
    return false
  }
}

class Student: Person, Classify {
  func isStudent() -> Bool {
    return true
  }
}

var s = Student(first_name: "Sam", last_name: "Scoth", age: 20)
var t = Mentor(first_name: "Alex", last_name: "Rap", age: 34)

if s.isStudent()
{
    print("\(s.fullName()) is student")
}
if t.isStudent()
{
    print("\(t.fullName()) is student")
}
