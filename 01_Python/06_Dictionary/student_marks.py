students = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78,
    "Riya": 88,
    "Karan": 95
}

for name, marks in students.items():
    print(name, ":", marks)

total = sum(students.values())
average = total / len(students)

print("Total Marks:", total)
print("Average Marks:", average)

highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print("Highest:", highest, students[highest])
print("Lowest:", lowest, students[lowest])

print("Students scoring above 85:")

for name, marks in students.items():
    if marks > 85:
        print(name, marks)