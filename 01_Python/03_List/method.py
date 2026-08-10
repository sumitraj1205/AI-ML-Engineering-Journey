numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

print("Length:", len(numbers))

print("First element:", numbers[0])
print("Last element:", numbers[-1])

numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.extend([70, 80])
print("After extend:", numbers)

numbers.remove(25)
print("After remove:", numbers)

removed = numbers.pop(2)
print("Removed element:", removed)
print("After pop:", numbers)

print("Index of 40:", numbers.index(40))

numbers.append(40)
print("Count of 40:", numbers.count(40))

numbers.sort()
print("Ascending order:", numbers)

numbers.sort(reverse=True)
print("Descending order:", numbers)

numbers.reverse()
print("After reverse:", numbers)

new_numbers = numbers.copy()
print("Copied list:", new_numbers)

new_numbers.clear()
print("After clear:", new_numbers)

numbers = [10, 20, 30, 40, 50]

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))

print("30 exists:", 30 in numbers)
print("100 does not exist:", 100 not in numbers)

print("First three:", numbers[:3])
print("Last three:", numbers[-3:])

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print("Combined:", combined)

list3 = [1, 2]
print("Repeated:", list3 * 3)

squares = [x ** 2 for x in numbers]
print("Squares:", squares)

text = "Python"
letters = list(text)
print("String to list:", letters)