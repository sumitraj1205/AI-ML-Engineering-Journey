# Problem: Check whether a subsequence with sum K exists.
# Approach: Use take and not-take recursion with early return.
# Time Complexity: O(2^n)
# Space Complexity: O(n)

def check_subsequence(index, arr, total, k):
    if index == len(arr):
        return total == k

    # Take the current element
    if check_subsequence(index + 1, arr, total + arr[index], k):
        return True

    # Do not take the current element
    if check_subsequence(index + 1, arr, total, k):
        return True

    return False


arr = [1, 2, 1]
k = 3

print(check_subsequence(0, arr, 0, k))