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

enum Subject {
  case Math
  case English
  case French
  case History
}
// var p = Person(first_name: "John", last_name: "Fring", age: 30)
//
// print("name: \(p.first_name)")
// print("fullName: \(p.fullName())")
class Mentor: Person, Classify {
  var subject: Subject

  init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
    self.subject = subject
    super.init(first_name: first_name, last_name: last_name, age: age)
  }

  func stringSubject() -> String {
    switch subject {
      case .Math: return "Math"
      case .English: return "English"
      case .French: return "French"
      case .History: return "History"
    }
  }

  func isStudent() -> Bool {
    return false
  }
}

class Student: Person, Classify {
  func isStudent() -> Bool {
    return true
  }
}

class School {
  var name: String
  var list_persons: [Person]

  init (name: String) {
    self.name = name
    self.list_persons = []
  }

  func addStudent(p: Person) -> Bool {
    if p is Student {
      list_persons.append(p)
      return true
    }
    return false
  }

  func addMentor(p: Person) -> Bool {
    if p is Mentor {
      list_persons.append(p)
      return true
    }
    return false
  }
}

// var s = Student(first_name: "Sam", last_name: "Scoth", age: 20)
// var m = Mentor(first_name: "Alex", last_name: "Rap", age: 34, subject: Subject.French)
//
// var school = School(name: "Holberton")
// if(school.addStudent(s)) {
//     print("\(s.fullName()) is now student in the school!")
// }
// if(school.addMentor(s)) {
//     print("\(s.fullName()) is now mentor in the school!")
// }
// if(school.addStudent(m)) {
//     print("\(m.fullName()) is now student in the school!")
// }
// if(school.addMentor(m)) {
//     print("\(m.fullName()) is now mentor in the school!")
// }

//
// var s = Student(first_name: "Sam", last_name: "Scoth", age: 20)
// var t = Mentor(first_name: "Alex", last_name: "Rap", age: 34)
//
// if s.isStudent()
// {
//     print("\(s.fullName()) is student")
// }
// if t.isStudent()
// {
//     print("\(t.fullName()) is student")
// }

// var s = Student(first_name: "Sam", last_name: "Scoth", age: 20)
// var m = Mentor(first_name: "Alex", last_name: "Rap", age: 34, subject: Subject.French)
//
// if s.isStudent()
// {
//     print("\(s.fullName()) is student")
// }
// if m.isStudent()
// {
//     print("\(m.fullName()) is student")
// }
// else
// {
//     print("\(m.fullName()) is mentor of \(m.stringSubject())")
// }
