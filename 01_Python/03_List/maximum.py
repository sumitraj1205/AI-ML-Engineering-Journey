numbers = [10, 50, 20, 80, 30]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum:", maximum)