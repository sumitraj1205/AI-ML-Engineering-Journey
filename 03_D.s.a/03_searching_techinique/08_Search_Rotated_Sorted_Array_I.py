# Search in Rotated Sorted Array I
#
# Problem:
# Given a rotated sorted array with distinct elements,
# search for a target value X.
# Return its index if present, otherwise return -1.
#
# Approach:
# At every step, one half of the array is sorted.
# Identify the sorted half.
# Check whether X lies inside that half.
# If yes, search that half.
# Otherwise, search the other half.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)


def search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid

        if arr[low] <= arr[mid]:

            if arr[low] <= x < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:

            if arr[mid] < x <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


arr = [4, 5, 6, 7, 0, 1, 2]
x = 0

print(search(arr, x))