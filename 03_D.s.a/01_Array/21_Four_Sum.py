# 4-Sum Problem
#
# Problem:
# Given an integer array and a target value,
# find all unique quadruplets whose sum is equal to the target.
#
# Approach:
# First sort the array.
#
# Fix two elements using two loops.
# Then use the two-pointer technique to find
# the remaining two elements.
#
# For every pair i and j:
# 1. Set left = j + 1.
# 2. Set right = n - 1.
# 3. Calculate the sum of four elements.
# 4. If sum == target, store the quadruplet.
# 5. If sum < target, move left forward.
# 6. If sum > target, move right backward.
#
# Skip duplicate values to avoid duplicate quadruplets.
#
# Time Complexity: O(n³)
# Space Complexity: O(1) excluding the result


def four_sum(arr, target):
    arr.sort()
    result = []

    n = len(arr)

    for i in range(n - 3):

        # Skip duplicate first elements
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, n - 2):

            # Skip duplicate second elements
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:

                total = arr[i] + arr[j] + arr[left] + arr[right]

                if total == target:
                    result.append(
                        [arr[i], arr[j], arr[left], arr[right]]
                    )

                    # Skip duplicates
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1

                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < target:
                    left += 1

                else:
                    right -= 1

    return result


arr = [1, 0, -1, 0, -2, 2]
target = 0

print(four_sum(arr, target))