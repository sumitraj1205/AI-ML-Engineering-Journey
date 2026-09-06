# Spiral Matrix
#
# Problem:
# Given a matrix, print all its elements in spiral order.
#
# Example:
#
# Input:
# 1 2 3
# 4 5 6
# 7 8 9
#
# Spiral Order:
# 1 2 3 6 9 8 7 4 5
#
# Approach:
# Maintain four boundaries:
#
# top
# bottom
# left
# right
#
# Traverse:
# 1. Left to right across the top.
# 2. Top to bottom along the right.
# 3. Right to left across the bottom.
# 4. Bottom to top along the left.
#
# After every traversal, move the corresponding boundary inward.
#
# Time Complexity: O(m * n)
# Space Complexity: O(m * n) for the result array


def spiral_order(matrix):

    result = []

    if not matrix:
        return result

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # Left to right
        for j in range(left, right + 1):
            result.append(matrix[top][j])

        top += 1

        # Top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])

        right -= 1

        # Right to left
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])

            bottom -= 1

        # Bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])

            left += 1

    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiral_order(matrix))