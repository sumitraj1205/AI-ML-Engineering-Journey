student = {
    "name": "Rahul",
    "age": 20,
    "branch": "CSE",
    "marks": 85
}

print("Dictionary:", student)
print("Name:", student["name"])
print("Age:", student["age"])
print("Branch:", student["branch"])
print("Marks:", student["marks"])

student["age"] = 21
print("After updating:", student)

student["city"] = "Kolkata"
print("After adding:", student)

student.pop("city")
print("After removing:", student)

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Length:", len(student))

print("name" in student)
print("city" in student)