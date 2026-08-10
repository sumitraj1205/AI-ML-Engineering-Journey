student = ("Darkrai", 21, "AI & ML")

name, age, branch = student

print("Name:", name)
print("Age:", age)
print("Branch:", branch)

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)

a, b = 10, 20

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)