# Lower Bound
#
# Problem:
# Given a sorted array and a number X, find the first index
# where an element greater than or equal to X occurs.
#
# If no such element exists, return the length of the array.
#
# Approach:
# Use Binary Search.
# If arr[mid] >= X, mid can be a possible answer,
# so search towards the left.
# Otherwise, search towards the right.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)


def lower_bound(arr, x):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            high = mid
        else:
            low = mid + 1

    return low


arr = [1, 2, 4, 4, 5, 7]
x = 4

print(lower_bound(arr, x))