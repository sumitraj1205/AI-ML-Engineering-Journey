# Problem: Count subsequences whose sum is equal to K.
# Approach: Add the counts of take and not-take recursion.
# Time Complexity: O(2^n)
# Space Complexity: O(n)

def count_subsequences(index, arr, total, k):
    if index == len(arr):
        if total == k:
            return 1
        return 0

    # Take the current element
    take = count_subsequences(
        index + 1, arr, total + arr[index], k
    )

    # Do not take the current element
    not_take = count_subsequences(
        index + 1, arr, total, k
    )

    return take + not_take


arr = [1, 2, 1]
k = 2

print(count_subsequences(0, arr, 0, k))