# Basics of Hashing
#
# Problem:
# Understand how hashing can be used to store and retrieve
# information efficiently.
#
# Approach:
# In Python, a dictionary works as a hash table.
# It stores data in key-value pairs.
#
# We can use a key to store a value and later retrieve
# that value using the same key.
#
# Average Time Complexity:
# Insert: O(1)
# Search: O(1)
# Delete: O(1)
#
# Space Complexity: O(n)


# Creating a hash table using a dictionary

student_marks = {
    "Sumit": 85,
    "Rahul": 90,
    "Aman": 78
}


# Accessing a value using its key

print(student_marks["Sumit"])


# Adding a new key-value pair

student_marks["Rohit"] = 88

print(student_marks)


# Updating an existing value

student_marks["Sumit"] = 95

print(student_marks)


# Checking whether a key exists

if "Rahul" in student_marks:
    print("Rahul is present")


# Removing a key-value pair

del student_marks["Aman"]

print(student_marks)