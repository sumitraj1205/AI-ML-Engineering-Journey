# 2D Matrix Basics
#
# Problem:
# Learn the basics of creating, accessing, traversing,
# and modifying elements in a 2D matrix.
#
# Approach:
# A matrix can be represented using a list of lists.
#
# Example:
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# The first index represents the row.
# The second index represents the column.
#
# Time Complexity:
# Accessing an element: O(1)
# Traversing the matrix: O(rows * columns)
#
# Space Complexity: O(rows * columns)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# Access an element

print("Element:", matrix[1][2])


# Traverse the matrix

for row in matrix:
    for element in row:
        print(element, end=" ")

print()


# Access using row and column indices

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        print(f"matrix[{i}][{j}] =", matrix[i][j])