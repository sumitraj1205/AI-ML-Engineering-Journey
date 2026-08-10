numbers = {10, 20, 30, 40, 50}

print("Set:", numbers)
print("Length:", len(numbers))

numbers.add(60)
print("After add:", numbers)

numbers.update([70, 80, 90])
print("After update:", numbers)

numbers.remove(30)
print("After remove:", numbers)

numbers.discard(100)
print("After discard:", numbers)

print("40 exists:", 40 in numbers)
print("100 exists:", 100 in numbers)

numbers.pop()
print("After pop:", numbers)

copy_set = numbers.copy()
print("Copied set:", copy_set)

numbers.clear()
print("After clear:", numbers)