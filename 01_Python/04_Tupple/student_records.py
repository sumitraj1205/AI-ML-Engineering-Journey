students = (
    ("Rahul", 20, "CSE", 85),
    ("Aman", 21, "AI & ML", 90),
    ("Priya", 20, "CSE", 88),
    ("Riya", 22, "ECE", 76)
)

print("Student Records:")

for student in students:
    print(student)

print("\nStudent Details:")

for name, age, branch, marks in students:
    print("Name:", name)
    print("Age:", age)
    print("Branch:", branch)
    print("Marks:", marks)
    print()

print("Students with marks above 85:")

for name, age, branch, marks in students:
    if marks > 85:
        print(name, marks)

print("Total Students:", len(students))

total_marks = 0

for name, age, branch, marks in students:
    total_marks += marks

average = total_marks / len(students)

print("Average Marks:", average)

highest = students[0]

for student in students:
    if student[3] > highest[3]:
        highest = student

print("Highest Marks:")
print("Name:", highest[0])
print("Marks:", highest[3])