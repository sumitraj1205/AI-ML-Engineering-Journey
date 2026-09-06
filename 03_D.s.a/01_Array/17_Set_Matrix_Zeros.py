# Set Matrix Zeros
#
# Problem:
# Given a matrix, if an element is 0, set its entire row
# and column to 0.
#
# Approach:
# First identify all rows and columns that contain zero.
#
# Store their indices in sets.
#
# Then traverse the matrix again and set an element to zero
# if its row or column contains a zero.
#
# Time Complexity: O(m * n)
# Space Complexity: O(m + n)


def set_zeroes(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    # Find rows and columns containing zero
    for i in range(rows):
        for j in range(cols):

            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Set corresponding rows and columns to zero
    for i in range(rows):
        for j in range(cols):

            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0


matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

set_zeroes(matrix)

for row in matrix:
    print(row)