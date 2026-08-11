file = open("students.txt", "a")

name = input("Enter student name: ")
age = input("Enter student age: ")
branch = input("Enter student branch: ")
marks = input("Enter student marks: ")

file.write(name + "," + age + "," + branch + "," + marks + "\n")

file.close()

print("Student record saved successfully.")

file = open("students.txt", "r")

print("\nStudent Records:")

for record in file:
    data = record.strip().split(",")

    print("Name:", data[0])
    print("Age:", data[1])
    print("Branch:", data[2])
    print("Marks:", data[3])
    print()

file.close()