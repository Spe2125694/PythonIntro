names = ["John", "Bob", "Spencer", "Sam", "Mary"]
names[0] = "Jon"
print(names)
print(names[0:2])
print(names)
print('')
print('')

numbers = [1, 2, 3, 4, 5]
numbers.insert(0, -1)
print(numbers)
numbers.remove(-1)
print(numbers)
print(1 in numbers)
print(10 in numbers)
print(len(numbers))
numbers.clear()
print(numbers)
