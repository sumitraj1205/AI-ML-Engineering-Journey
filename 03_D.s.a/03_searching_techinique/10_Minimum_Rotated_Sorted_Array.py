# Find Minimum in Rotated Sorted Array
#
# Problem:
# Given a rotated sorted array containing distinct elements,
# find the minimum element.
#
# Approach:
# Compare arr[mid] with arr[high].
#
# If arr[mid] > arr[high], the minimum lies in the right half.
# Otherwise, the minimum is at mid or in the left half.
#
# Continue until low and high point to the same element.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)


def find_min(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return arr[low]


arr = [4, 5, 6, 7, 0, 1, 2]

print(find_min(arr))