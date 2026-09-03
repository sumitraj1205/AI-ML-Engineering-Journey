# Kadane's Algorithm - Maximum Subarray Sum
#
# Problem:
# Given an integer array, find the maximum possible sum
# of a contiguous subarray.
#
# Approach:
# Kadane's Algorithm keeps track of:
#
# current_sum -> maximum sum ending at the current position
# max_sum     -> maximum sum found so far
#
# At every element, decide whether to:
# 1. Start a new subarray from the current element.
# 2. Extend the previous subarray.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


def max_subarray_sum(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):

        current_sum = max(arr[i], current_sum + arr[i])

        max_sum = max(max_sum, current_sum)

    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_subarray_sum(arr))