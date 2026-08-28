# Insertion Sort
#
# Problem:
# Given an array, sort the array in ascending order using Insertion Sort.
#
# Approach:
# Maintain a sorted portion on the left side of the array.
# Pick the current element as the key.
# Shift all elements greater than the key one position to the right.
# Insert the key into its correct position.
#
# Time Complexity:
# Best Case: O(n)
# Average Case: O(n²)
# Worst Case: O(n²)
#
# Space Complexity: O(1)


def insertion_sort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = [12, 11, 13, 5, 6]

print(insertion_sort(arr))