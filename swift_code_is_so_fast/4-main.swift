
var numbers = [4, 7, 1, 9, 6, 5, 6, 9]

let max = numbers.reduce(0, combine:{if $0 > $1 {
  return $0
} else {
  return $1
}})

print(max)
