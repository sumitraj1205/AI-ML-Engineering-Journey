def find_largest(a, b):
    if a > b:
        return a
    else:
        return b


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Largest number is:", find_largest(x, y))