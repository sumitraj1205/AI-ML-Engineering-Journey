numbers = [10, 50, 20, 80, 30]

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum:", minimum)