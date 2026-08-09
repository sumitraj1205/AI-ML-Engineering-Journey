for i in range(1, 11):
    print(i)

for i in range(2, 21, 2):
    print(i)

total = 0

for i in range(1, 11):
    total += i

print("Sum:", total)


number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


count = 1

while count <= 10:
    print(count)
    count += 1
