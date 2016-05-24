class Person: CustomStringConvertible {
  var first_name: String
  var last_name: String
  var age: Int
  var description: String

  init(first_name: String, last_name: String, age: Int) {
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.description = ""
    self.description = self.fullName()
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

  func listStudents() -> [Person] {
    return list_persons.filter({$0 is Student}).sort {return $0.age < $1.age}
  }

  func listMentors() -> [Person] {
    return list_persons.filter({$0 is Mentor}).sort {return $0.age < $1.age}
  }

  // The spec for this function contradicts the provided tests.
  func listMentorsBySubject() -> [Person] {
    return list_persons.filter({$0 is Mentor}).sort {return $0.age < $1.age}
  }

  func mentorsAgeAverage() -> Int {
    let mentors = self.listMentors()
    if mentors.count < 1 {
      return 0
    } else if mentors.count == 1 {
      return mentors[0].age
    } else { 
      return mentors.reduce(0, combine:{
        (first: Int, second: Person) -> Int in
        return first + second.age
      }) / mentors.count
    }
  }


  func mentorsAgeAverge() -> Int {
     return self.mentorsAgeAverage()
  }

  func studentsAgeAverage() -> Int {
    let students = self.listStudents()
    if students.count < 1 {
      return 0
    } else if students.count == 1 {
      return students[0].age
    } else {
      return students.reduce(0, combine:{
        (first: Int, second: Person) -> Int in
        return first + second.age
      }) / students.count
    }
  }

  func studentsAgeAverge() -> Int {
    return self.studentsAgeAverage()
  }
}

