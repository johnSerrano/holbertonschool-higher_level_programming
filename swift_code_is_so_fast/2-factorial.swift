func factorial(N: Int) -> Int {
  if N == 1 {
    return N
  }
  return N * factorial(N-1)
}

// print("Factorial 3 is \(factorial(3))")
// print("Factorial 7 is \(factorial(7))")
// print("Factorial 18 is \(factorial(12))")
