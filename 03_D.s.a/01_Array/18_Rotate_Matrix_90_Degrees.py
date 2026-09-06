# Rotate Matrix by 90 Degrees
#
# Problem:
# Given an n x n matrix, rotate the matrix by 90 degrees clockwise.
#
# Approach:
# The rotation can be performed in two steps:
#
# 1. Transpose the matrix.
# 2. Reverse every row.
#
# Example:
#
# Original:
# 1 2 3
# 4 5 6
# 7 8 9
#
# After rotation:
# 7 4 1
# 8 5 2
# 9 6 3
#
# Time Complexity: O(n²)
# Space Complexity: O(1)


def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse every row
    for row in matrix:
        row.reverse()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate(matrix)

for row in matrix:
    print(row)