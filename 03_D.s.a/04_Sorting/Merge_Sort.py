# Merge Sort
#
# Problem:
# Given an array, sort the array in ascending order using Merge Sort.
#
# Approach:
# Merge Sort follows the Divide and Conquer approach.
#
# 1. Divide the array into two halves.
# 2. Recursively sort both halves.
# 3. Merge the two sorted halves.
#
# Time Complexity:
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n log n)
#
# Space Complexity: O(n)


def merge(arr, low, mid, high):
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    i = 0
    j = 0
    k = low

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, low, high):

    if low >= high:
        return

    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)

    merge(arr, low, mid, high)


arr = [38, 27, 43, 3, 9, 82, 10]

merge_sort(arr, 0, len(arr) - 1)

print(arr)