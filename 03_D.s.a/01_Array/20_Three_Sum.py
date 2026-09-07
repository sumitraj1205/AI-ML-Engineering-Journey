# 3-Sum Problem
#
# Problem:
# Given an integer array, find all unique triplets
# whose sum is equal to 0.
#
# Approach:
# First sort the array.
#
# Fix one element and use the two-pointer technique
# to find the other two elements.
#
# For every index i:
# 1. Set left = i + 1.
# 2. Set right = n - 1.
# 3. Calculate the sum of arr[i], arr[left], and arr[right].
# 4. If sum == 0, store the triplet.
# 5. If sum < 0, move left forward.
# 6. If sum > 0, move right backward.
#
# Skip duplicate values to avoid duplicate triplets.
#
# Time Complexity: O(n²)
# Space Complexity: O(1) excluding the result


def three_sum(arr):
    arr.sort()
    result = []

    n = len(arr)

    for i in range(n - 2):

        # Skip duplicate first elements
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:

            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                result.append([arr[i], arr[left], arr[right]])

                # Skip duplicates
                while left < right and arr[left] == arr[left + 1]:
                    left += 1

                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return result


arr = [-1, 0, 1, 2, -1, -4]

print(three_sum(arr))