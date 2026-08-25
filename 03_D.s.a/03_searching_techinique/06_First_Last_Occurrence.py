# First and Last Occurrence
#
# Problem:
# Given a sorted array containing duplicate elements,
# find the first and last occurrence of a given number X.
#
# Approach:
# For the first occurrence, when X is found, store the index
# and continue searching towards the left.
#
# For the last occurrence, when X is found, store the index
# and continue searching towards the right.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)


def first_occurrence(arr, x):
    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            answer = mid
            high = mid - 1

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return answer


def last_occurrence(arr, x):
    low = 0
    high = len(arr) - 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            answer = mid
            low = mid + 1

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return answer


arr = [1, 2, 2, 2, 3, 4, 5]
x = 2

print("First:", first_occurrence(arr, x))
print("Last:", last_occurrence(arr, x))