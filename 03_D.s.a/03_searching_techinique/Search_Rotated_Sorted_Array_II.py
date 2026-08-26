# Search in Rotated Sorted Array II
#
# Problem:
# Given a rotated sorted array that may contain duplicates,
# determine whether a target value X exists.
#
# Approach:
# The approach is similar to Rotated Sorted Array I.
# However, duplicates can make it impossible to determine
# which half is sorted.
#
# When arr[low] == arr[mid] == arr[high],
# shrink the search space by moving both boundaries inward.
# Otherwise, identify the sorted half and continue Binary Search.
#
# Average Time Complexity: O(log n)
# Worst-case Time Complexity: O(n)
# Space Complexity: O(1)


def search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return True

        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue

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

    return False


arr = [2, 5, 6, 0, 0, 1, 2]
x = 0

print(search(arr, x))